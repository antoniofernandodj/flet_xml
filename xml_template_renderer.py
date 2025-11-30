# xml_template_renderer.py
import copy
import xml.etree.ElementTree as ET
import ast
from typing import Any, Dict, Tuple, List

# ---------- Configuração ----------
# Expressões serão avaliadas com esses builtins permitidos (poucos).
SAFE_BUILTINS = {
    "len": len,
    "min": min,
    "max": max,
    "sum": sum,
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "enumerate": enumerate,
    "range": range,
}

# ---------- Funções utilitárias ----------
def safe_eval(expr: str, context: Dict[str, Any]) -> Any:
    """
    Avalia uma expressão Python de forma limitada.
    - expr: expressão Python (string)
    - context: dicionário com variáveis locais/ambientais
    """
    # Remove chaves se o usuário usar a sintaxe {expr}
    if expr.startswith("{") and expr.endswith("}"):
        expr = expr[1:-1].strip()

    # Compila para checar sintaxe
    node = ast.parse(expr, mode="eval")
    code = compile(node, "<template>", "eval")
    return eval(code, {"__builtins__": SAFE_BUILTINS}, context)


def expr_in_string(s: str) -> bool:
    """Retorna True se a string contém {expr} simples"""
    return "{" in s and "}" in s


def eval_in_text(s: str, context: Dict[str, Any]) -> str:
    """
    Substitui todas as ocorrências de {expr} em uma string por sua avaliação.
    Ex: "Olá {user['name']}" -> "Olá Antonio"
    """
    out = ""
    i = 0
    while i < len(s):
        start = s.find("{", i)
        if start == -1:
            out += s[i:]
            break
        end = s.find("}", start + 1)
        if end == -1:
            # não bem formado — quebra
            out += s[i:]
            break
        out += s[i:start]
        expr = s[start + 1:end].strip()
        try:
            val = safe_eval(expr, context)
        except Exception as e:
            raise RuntimeError(f"Erro ao avaliar expressão '{expr}': {e}")
        out += "" if val is None else str(val)
        i = end + 1
    return out


# ---------- Processamento de diretivas ----------
def _process_node(node: ET.Element, context: Dict[str, Any]) -> List[ET.Element]:
    """
    Processa um elemento e retorna lista de elementos resultantes (0..n),
    permitindo py-for produzir múltiplos clones.
    """
    # 1) py-if
    py_if = node.attrib.pop("py-if", None)
    if py_if is not None:
        condition = safe_eval(py_if, context)
        if not condition:
            return []  # remove o nó inteiro

    # 2) py-for
    py_for = node.attrib.pop("py-for", None)
    if py_for is not None:
        # sintaxe esperada: "item in items" ou "k, v in something.items()"
        # vamos suportar qualquer assignment do lado esquerdo
        parts = py_for.split(" in ", 1)
        if len(parts) != 2:
            raise ValueError(f"py-for mal formado: {py_for}")
        left, right = parts[0].strip(), parts[1].strip()
        iterable = safe_eval(right, context)
        results = []
        for item in iterable:
            # cria cópia profunda do node
            ctx_copy = dict(context)  # cada iteração tem seu contexto
            # atribui left = item; suporta multiple targets
            # exemplo left = "k, v"
            if "," in left:
                names = [n.strip() for n in left.split(",")]
                # se item for tupla/iterable, desempacota
                try:
                    a_values = list(item)
                except TypeError:
                    raise ValueError(f"py-for: item '{item}' não é iterável para desempacotar em {names}")
                if len(a_values) != len(names):
                    raise ValueError(f"py-for: desempacotamento incompatível para {left} <- {item}")
                for nm, val in zip(names, a_values):
                    ctx_copy[nm] = val
            else:
                ctx_copy[left] = item

            node_clone = copy.deepcopy(node)
            # Processa o clone recursivamente usando ctx_copy
            processed_children = []
            for child in list(node_clone):
                node_clone.remove(child)
                children_result = _process_node(child, ctx_copy)
                for c in children_result:
                    node_clone.append(c)

            # Process attributes/text of the clone with ctx_copy
            _process_attribs_and_text(node_clone, ctx_copy)
            results.append(node_clone)
        return results

    # 3) py-set
    py_set = node.attrib.pop("py-set", None)
    if py_set is not None:
        # aceita múltiplas instruções separadas por ;
        # ex: "a=1; b=items[0]"
        assignments = [p.strip() for p in py_set.split(";") if p.strip()]
        for assign in assignments:
            # avalia como expressão de atribuição simples
            if "=" not in assign:
                raise ValueError(f"py-set espera atribuições, encontrou: {assign}")
            left, right = assign.split("=", 1)
            left = left.strip()
            right = right.strip()
            value = safe_eval(right, context)
            context[left] = value

    # 4) processa filhos recursivamente
    for child in list(node):
        node.remove(child)
        processed = _process_node(child, context)
        for c in processed:
            node.append(c)

    # 5) processa atributos e texto do próprio nó (substitui {expr})
    _process_attribs_and_text(node, context)

    return [node]

def prettify_xml(xml_str: str) -> str:
    """
    Recebe uma string XML e retorna o XML identado e formatado.
    """
    from xml.dom.minidom import parseString

    try:
        dom = parseString(xml_str)
        result = dom.toprettyxml(indent="  ")
        result = '\n'.join([l for l in result.split('\n') if l.strip()])
        return result
    except Exception as e:
        raise ValueError(f"Erro ao formatar XML: {e}")


def _process_attribs_and_text(node: ET.Element, context: Dict[str, Any]) -> None:
    # Atributos: se contém {expr} avalia
    for k, v in list(node.attrib.items()):
        if v is None:
            continue
        if expr_in_string(v):
            node.attrib[k] = eval_in_text(v, context)

    # Texto do nó (node.text)
    if node.text and expr_in_string(node.text):
        node.text = eval_in_text(node.text, context)

    # tail text (texto após o elemento)
    if node.tail and expr_in_string(node.tail):
        node.tail = eval_in_text(node.tail, context)


def render_xml_template(xml_string: str, context: Dict[str, Any]) -> str:
    """
    Renderiza o XML com diretivas py-*, retornando string XML sem diretivas.
    """
    # Envolve em root se necessário
    wrapped = f"<root>{xml_string}</root>"
    try:
        root = ET.fromstring(wrapped)
    except ET.ParseError as e:
        raise

    new_children = []
    for child in list(root):
        root.remove(child)
        processed = _process_node(child, dict(context))
        for c in processed:
            new_children.append(c)

    # monta uma nova árvore apenas com os nós processados
    out_root = ET.Element("root")
    for c in new_children:
        out_root.append(c)

    # retorna conteúdo interno (sem a tag root)
    string = "".join(ET.tostring(c, encoding="unicode") for c in out_root)
    return prettify_xml(string)


# ---------- Exemplo rápido ----------
if __name__ == "__main__":
    xml = """
    <div>
        <p py-if="{user['active']}">Olá {user['name']}</p>
            <ul>
        <li py-for="item in items">{item}</li>
        </ul>
        <span py-set="x=10">{x}</span>
    </div>
    """
    ctx = {"user": {"active": False, "name": "Ana"}, "items": [1, 2, 3]}
    print(render_xml_template(xml, ctx))
