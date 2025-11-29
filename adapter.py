import ast
import inspect
import xml.etree.ElementTree as ET
from typing import Any, Callable, Dict, Optional

import flet  # type: ignore
from flet import Page
from jinja2 import Environment, FileSystemLoader

# mapeamento de tag -> nome do parâmetro de filhos
CHILD_ATTRS = {
    "Column": "controls",
    "Row": "controls",
    "Stack": "controls",
    "ListView": "controls",
    "Tabs": "tabs",
    "Dropdown": "options",   # <- Dropdown usa `options`
}

# Tipos de campos que podem ter valores extraídos
FIELD_TYPES = {
    "TextField", "Text", "Dropdown", "Checkbox", 
    "Switch", "Slider", "Radio", "RadioGroup"
}


class XMLFletAdapter:
    def __init__(
        self,
        template_name: str,
        handlers: dict[str, Callable],
        title: str,
        templates_dir: str = "templates",
        context = {}
    ):
        """
        template_name: arquivo .xml (na pasta templates/) com sintaxe Jinja
        handlers: dicionário de callbacks { "nome": func }
        title: título da página
        templates_dir: pasta onde ficam os templates (default: templates/)
        context: contexto para renderização do template Jinja
        """
        self.template_name = template_name
        self.handlers = handlers
        self.title = title
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.context = context
        self.fields: Dict[str, Any] = {}  # Armazena referências aos campos por id/name
        self.page: Optional[Page] = None

    def __call__(self, page: Page):
        self.page = page
        page.title = self.title
        self.fields.clear()  # Limpa campos anteriores
        
        # Armazena referência ao adapter na página para acesso nos callbacks
        # Garante que page.data seja um dicionário
        if not hasattr(page, 'data') or page.data is None or not isinstance(page.data, dict):
            page.data = {}
        page.data['adapter'] = self

        # Renderiza o template Jinja
        template = self.env.get_template(self.template_name)
        xml_string = template.render(self.context)

        widgets = self.parse_xml_string(xml_string, handlers=self.handlers)
        for w in widgets:
            page.add(w)

    def _parse_attr_value(self, val: str) -> Any:
        if val is None:
            return None
        s = val.strip()
        if s == "":
            return ""
        if s.lower() in ("true", "false"):
            return s.lower() == "true"
        try:
            return ast.literal_eval(s)
        except Exception:
            return s

    def _get_class(self, tag: str):
        cls = getattr(flet, tag, None)
        if cls is not None:
            return cls
        if "." in tag:
            mod, name = tag.split(".", 1)
            submodule = getattr(flet, mod, None)
            if submodule:
                return getattr(submodule, name, None)
        return None

    def _bind_event(self, obj: Any, event_name: str, handler: Callable):
        if hasattr(obj, event_name):
            try:
                setattr(obj, event_name, handler)
                return True
            except Exception:
                return False
        return False

    def _get_field_value(self, field: Any) -> Any:
        """Extrai o valor de um campo baseado no seu tipo"""
        if hasattr(field, 'value'):
            return field.value
        elif hasattr(field, 'text'):
            return field.text
        elif hasattr(field, 'data'):
            return field.data
        return None

    def get_field_data(self, field_ids: Optional[list[str]] = None) -> Dict[str, Any]:
        """
        Retorna um dicionário com os valores dos campos identificados.
        
        Args:
            field_ids: Lista de IDs/names dos campos a retornar. 
                      Se None, retorna todos os campos.
        
        Returns:
            Dicionário {id: value} com os valores dos campos
        """
        if field_ids is None:
            field_ids = list(self.fields.keys())
        
        data = {}
        for field_id in field_ids:
            if field_id in self.fields:
                field = self.fields[field_id]
                data[field_id] = self._get_field_value(field)
        return data

    def get_field(self, field_id: str) -> Optional[Any]:
        """
        Retorna a referência direta a um campo específico.
        
        Args:
            field_id: ID ou name do campo
        
        Returns:
            Referência ao campo ou None se não encontrado
        """
        return self.fields.get(field_id)

    def _create_callback_wrapper(self, original_handler: Callable) -> Callable:
        """Cria um wrapper para o callback que passa os dados dos campos"""
        def wrapper(e: flet.ControlEvent):
            # Passa o evento original e os dados dos campos
            field_data = self.get_field_data()
            # Tenta chamar com os dados dos campos se o handler aceitar
            try:
                sig = inspect.signature(original_handler)
                params = list(sig.parameters.keys())
                if len(params) > 1:
                    # Handler aceita mais de um parâmetro, passa os dados
                    return original_handler(e, field_data)
                else:
                    # Handler aceita apenas o evento
                    return original_handler(e)
            except Exception:
                # Fallback: chama apenas com o evento
                return original_handler(e)
        return wrapper

    def _instantiate_element(self, elem: ET.Element, handlers: Optional[Dict[str, Callable]] = None):
        tag = elem.tag
        cls = self._get_class(tag)

        kwargs: Dict[str, Any] = {}
        field_id = None  # ID ou name do campo para armazenar referência
        
        for k, v in elem.attrib.items():
            if k.startswith("on_"):
                kwargs[k] = v
                continue
            # Captura id ou name para armazenar referência ao campo (mas não adiciona aos kwargs)
            if k in ("id", "name") and tag in FIELD_TYPES:
                field_id = v
                continue  # Não adiciona id/name aos kwargs do widget
            kwargs[k] = self._parse_attr_value(v)

        children = []
        text_content = (elem.text or "").strip()
        for child in elem:
            if child.tag is ET.Comment:
                continue
            children.append(self._instantiate_element(child, handlers))

        if cls is None:
            raise ValueError(f"Tag desconhecida no flet: '{tag}'.")

        event_attrs = {k: v for k, v in kwargs.items() if k.startswith("on_")}
        for k in list(kwargs.keys()):
            if k.startswith("on_"):
                del kwargs[k]

        sig = None
        try:
            sig = inspect.signature(cls)
        except (ValueError, TypeError):
            pass

        passed_children_kwargs = {}
        if children:
            if sig and "controls" in sig.parameters:
                passed_children_kwargs["controls"] = children
            elif sig and "content" in sig.parameters:
                passed_children_kwargs["content"] = children[0] if len(children) == 1 else flet.Column(controls=children)
            elif sig and "children" in sig.parameters:
                passed_children_kwargs["children"] = children
            else:
                passed_children_kwargs["controls"] = children

        if text_content:
            if sig and "text" in sig.parameters:
                kwargs.setdefault("text", text_content)
            elif sig and "value" in sig.parameters:
                kwargs.setdefault("value", text_content)

        child_attr = CHILD_ATTRS.get(tag)
        try:
            if child_attr:
                instance = cls(**kwargs, **{child_attr: children})
            else:
                instance = cls(**kwargs, **passed_children_kwargs)
        except TypeError as e:
            raise TypeError(f"Erro ao criar {tag}: {e}")

        # Armazena referência ao campo se tiver id/name
        if field_id:
            self.fields[field_id] = instance

        # Processa eventos e cria wrappers para callbacks
        for ev_name, ev_val in event_attrs.items():
            handler = handlers.get(ev_val) if handlers else None
            if handler:
                # Cria wrapper que passa os dados dos campos
                wrapped_handler = self._create_callback_wrapper(handler)
                self._bind_event(instance, ev_name, wrapped_handler)

        return instance

    def parse_xml_string(self, xml_string: str, handlers: Optional[Dict[str, Callable]] = None):
        root = ET.fromstring(f"<root>{xml_string}</root>")
        widgets = []
        for child in root:
            widgets.append(self._instantiate_element(child, handlers))
        return widgets
