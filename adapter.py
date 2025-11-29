import ast
import inspect
import logging
import xml.etree.ElementTree as ET
from typing import Any, Callable, Dict, List, Optional

import flet  # type: ignore
from flet import Page
from jinja2 import Environment, FileSystemLoader

# Configuração de logging
logger = logging.getLogger(__name__)

# Mapeamento de tag -> nome do parâmetro de filhos
CHILD_ATTRS = {
    "Column": "controls",
    "Row": "controls",
    "Stack": "controls",
    "ListView": "controls",
    "Tabs": "tabs",
    "Dropdown": "options",
    "DataTable": "columns",
    "DataRow": "cells",
    "ExpansionTile": "controls",
    "ExpansionPanel": "content",
}

# Tipos de campos que podem ter valores extraídos
FIELD_TYPES = {
    "TextField",
    "Text",
    "Dropdown",
    "Checkbox",
    "Switch",
    "Slider",
    "Radio",
    "RadioGroup",
    "DatePicker",
    "TimePicker",
    "FilePicker",
    "ColorPicker",
    "SegmentedButton",
    "CupertinoTextField",
    "SearchBar",
}


class XMLFletAdapter:
    """
    Adaptador que converte templates XML com sintaxe Jinja2 em widgets Flet.
    
    Permite criar interfaces Flet usando XML declarativo, facilitando
    a separação entre lógica e apresentação.
    """
    
    def __init__(
        self,
        template_name: str,
        handlers: Dict[str, Callable],
        title: str,
        templates_dir: str = "templates",
        context: Optional[Dict[str, Any]] = None,
    ):
        """
        Inicializa o adaptador XML-Flet.
        
        Args:
            template_name: Nome do arquivo XML/Jinja2 na pasta de templates
            handlers: Dicionário de callbacks { "nome_handler": função }
            title: Título da janela da aplicação
            templates_dir: Diretório onde estão os templates (default: "templates")
            context: Contexto para renderização do template Jinja2
        
        Raises:
            ValueError: Se template_name estiver vazio ou handlers for inválido
        """
        if not template_name:
            raise ValueError("template_name não pode estar vazio")
        
        if not isinstance(handlers, dict):
            raise ValueError("handlers deve ser um dicionário")
        
        self.template_name = template_name
        self.handlers = handlers
        self.title = title
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.context = context or {}
        self.fields: Dict[str, Any] = {}  # Armazena referências aos campos por id/name
        self.page: Optional[Page] = None
        
        logger.debug(f"XMLFletAdapter inicializado: template={template_name}, handlers={list(handlers.keys())}")

    def __call__(self, page: Page) -> None:
        """
        Método chamado pelo Flet para inicializar a página.
        
        Args:
            page: Instância da página Flet
        """
        self.page = page
        page.title = self.title
        self.fields.clear()  # Limpa campos anteriores
        
        # Armazena referência ao adapter na página para acesso nos callbacks
        # Garante que page.data seja um dicionário
        if not hasattr(page, 'data') or page.data is None or not isinstance(page.data, dict):
            page.data = {}
        page.data['adapter'] = self

        try:
            # Renderiza o template Jinja
            template = self.env.get_template(self.template_name)
            xml_string = template.render(self.context)
            
            logger.debug(f"Template renderizado: {len(xml_string)} caracteres")
        except Exception as e:
            logger.error(f"Erro ao renderizar template '{self.template_name}': {e}")
            raise

        try:
            widgets = self.parse_xml_string(xml_string, handlers=self.handlers)
            for w in widgets:
                page.add(w)
            logger.info(f"Interface carregada: {len(self.fields)} campos registrados")
        except Exception as e:
            logger.error(f"Erro ao processar XML: {e}")
            raise

    def _parse_attr_value(self, val: str) -> Any:
        """
        Converte uma string de atributo XML para o tipo Python apropriado.
        
        Suporta:
        - Booleanos (true/false)
        - Números (int, float)
        - None/null
        - Listas e dicionários Python
        - Cores hexadecimais (#rrggbb, #rrggbbaa)
        - Strings (fallback)
        """
        if val is None:
            return None
        
        s = val.strip()
        if s == "":
            return ""
        
        # Booleanos
        if s.lower() in ("true", "false"):
            return s.lower() == "true"
        
        # None/null
        if s.lower() in ("none", "null"):
            return None
        
        # Números
        try:
            # Tenta int primeiro
            if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
                return int(s)
        except ValueError:
            pass
        
        try:
            # Tenta float
            return float(s)
        except ValueError:
            pass
        
        # Cores hexadecimais (#rrggbb ou #rrggbbaa)
        if s.startswith("#") and len(s) in (7, 9) and all(c in "0123456789abcdefABCDEF" for c in s[1:]):
            return s
        
        # Listas e dicionários Python
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            pass
        
        # String como fallback
        return s

    def _get_class(self, tag: str) -> Optional[type]:
        """
        Obtém a classe Flet correspondente a uma tag XML.
        
        Suporta:
        - Tags diretas: "Column" -> flet.Column
        - Tags com namespace: "dropdown.Option" -> flet.dropdown.Option
        
        Args:
            tag: Nome da tag XML
        
        Returns:
            Classe Flet correspondente ou None se não encontrada
        """
        # Tenta obter diretamente do módulo flet
        cls = getattr(flet, tag, None)
        if cls is not None:
            return cls
        
        # Tenta obter de um submódulo (ex: dropdown.Option)
        if "." in tag:
            mod, name = tag.split(".", 1)
            submodule = getattr(flet, mod, None)
            if submodule:
                cls = getattr(submodule, name, None)
                if cls is not None:
                    return cls
        
        return None

    def _bind_event(self, obj: Any, event_name: str, handler: Callable) -> bool:
        """
        Vincula um handler a um evento de um objeto.
        
        Args:
            obj: Objeto Flet que receberá o handler
            event_name: Nome do evento (ex: "on_click")
            handler: Função callback
        
        Returns:
            True se o evento foi vinculado com sucesso, False caso contrário
        """
        if not hasattr(obj, event_name):
            logger.warning(f"Objeto {type(obj).__name__} não possui evento '{event_name}'")
            return False
        
        try:
            setattr(obj, event_name, handler)
            return True
        except Exception as e:
            logger.error(f"Erro ao vincular evento '{event_name}': {e}")
            return False

    def _get_field_value(self, field: Any) -> Any:
        """
        Extrai o valor de um campo baseado no seu tipo.
        
        Tenta diferentes atributos comuns do Flet:
        - value: usado pela maioria dos campos
        - text: usado por Text e similares
        - data: usado por alguns componentes
        """
        if field is None:
            return None
        
        if hasattr(field, 'value'):
            return field.value
        elif hasattr(field, 'text'):
            return field.text
        elif hasattr(field, 'data'):
            return field.data
        elif hasattr(field, 'selected_index'):
            # Para componentes que usam índice selecionado
            return field.selected_index
        
        logger.warning(f"Campo {type(field).__name__} não possui atributo de valor conhecido")
        return None

    def get_field_data(self, field_ids: Optional[List[str]] = None) -> Dict[str, Any]:
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
            else:
                logger.warning(f"Campo '{field_id}' não encontrado")
        
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
    
    def set_field_value(self, field_id: str, value: Any) -> bool:
        """
        Define o valor de um campo e atualiza a interface.
        
        Args:
            field_id: ID ou name do campo
            value: Valor a ser definido
        
        Returns:
            True se o campo foi atualizado com sucesso, False caso contrário
        """
        field = self.get_field(field_id)
        if field is None:
            logger.warning(f"Campo '{field_id}' não encontrado")
            return False
        
        try:
            if hasattr(field, 'value'):
                field.value = value
            elif hasattr(field, 'text'):
                field.text = value
            elif hasattr(field, 'data'):
                field.data = value
            else:
                logger.warning(f"Campo '{field_id}' não possui atributo modificável conhecido")
                return False
            
            if self.page:
                field.update()
            return True
        except Exception as e:
            logger.error(f"Erro ao atualizar campo '{field_id}': {e}")
            return False
    
    def clear_fields(self, field_ids: Optional[List[str]] = None) -> int:
        """
        Limpa os valores dos campos especificados.
        
        Args:
            field_ids: Lista de IDs/names dos campos a limpar.
                      Se None, limpa todos os campos.
        
        Returns:
            Número de campos limpos com sucesso
        """
        if field_ids is None:
            field_ids = list(self.fields.keys())
        
        cleared = 0
        for field_id in field_ids:
            field = self.get_field(field_id)
            if field is None:
                continue
            
            try:
                if hasattr(field, 'value'):
                    # Tenta determinar o tipo de valor padrão
                    if isinstance(field.value, bool):
                        field.value = False
                    elif isinstance(field.value, (int, float)):
                        field.value = 0
                    elif isinstance(field.value, str):
                        field.value = ""
                    else:
                        field.value = None
                elif hasattr(field, 'text'):
                    field.text = ""
                elif hasattr(field, 'data'):
                    field.data = None
                
                if self.page:
                    field.update()
                cleared += 1
            except Exception as e:
                logger.error(f"Erro ao limpar campo '{field_id}': {e}")
        
        return cleared
    
    def update_all_fields(self) -> None:
        """Atualiza todos os campos na interface."""
        if not self.page:
            return
        
        for field in self.fields.values():
            try:
                field.update()
            except Exception as e:
                logger.error(f"Erro ao atualizar campo: {e}")
    
    def navigate_to(
        self,
        template_name: str,
        handlers: Optional[Dict[str, Callable]] = None,
        title: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Navega para uma nova página carregando um template diferente.
        
        Args:
            template_name: Nome do template a ser carregado
            handlers: Handlers para a nova página (usa os atuais se None)
            title: Título da nova página (mantém o atual se None)
            context: Contexto para o template (mescla com o atual se fornecido)
        """
        if not self.page:
            logger.error("Não é possível navegar: página não inicializada")
            return
        
        # Limpa a página atual
        self.page.clean()
        self.fields.clear()
        
        # Atualiza configurações
        if title:
            self.page.title = title
            self.title = title
        
        if handlers:
            self.handlers = handlers
        
        if context:
            # Mescla com o contexto atual
            self.context = {**self.context, **context}
        
        # Atualiza o template
        self.template_name = template_name
        
        try:
            # Renderiza o novo template
            template = self.env.get_template(template_name)
            xml_string = template.render(self.context)
            
            logger.debug(f"Navegando para template '{template_name}'")
        except Exception as e:
            logger.error(f"Erro ao renderizar template '{template_name}': {e}")
            raise
        
        try:
            widgets = self.parse_xml_string(xml_string, handlers=self.handlers)
            for w in widgets:
                self.page.add(w)
            logger.info(f"Página '{template_name}' carregada com sucesso")
        except Exception as e:
            logger.error(f"Erro ao processar XML do template '{template_name}': {e}")
            raise

    def _create_callback_wrapper(self, original_handler: Callable) -> Callable:
        """
        Cria um wrapper para o callback que automaticamente passa os dados dos campos.
        
        O wrapper detecta a assinatura do handler:
        - Se aceitar 2 parâmetros: passa (event, field_data)
        - Se aceitar 1 parâmetro: passa apenas (event)
        
        Args:
            original_handler: Função callback original
        
        Returns:
            Função wrapper que será chamada pelos eventos
        """
        def wrapper(e: flet.ControlEvent):
            try:
                # Tenta obter a assinatura do handler
                sig = inspect.signature(original_handler)
                params = list(sig.parameters.keys())
                
                if len(params) > 1:
                    # Handler aceita mais de um parâmetro, passa os dados dos campos
                    field_data = self.get_field_data()
                    return original_handler(e, field_data)
                else:
                    # Handler aceita apenas o evento
                    return original_handler(e)
            except (ValueError, TypeError) as e:
                # Erro ao inspecionar assinatura, tenta chamar apenas com evento
                logger.warning(f"Erro ao inspecionar handler '{original_handler.__name__}': {e}")
                try:
                    return original_handler(e)
                except Exception as ex:
                    logger.error(f"Erro ao executar handler: {ex}")
                    raise
            except Exception as e:
                # Outro erro, loga e propaga
                logger.error(f"Erro inesperado no wrapper do handler: {e}")
                raise
        
        return wrapper

    def _instantiate_element(self, elem: ET.Element, handlers: Optional[Dict[str, Callable]] = None) -> Any:
        """
        Converte um elemento XML em um widget Flet.
        
        Processa atributos, filhos, eventos e registra campos com id/name.
        
        Args:
            elem: Elemento XML a ser convertido
            handlers: Dicionário de handlers de eventos (opcional)
        
        Returns:
            Instância do widget Flet criado
        
        Raises:
            ValueError: Se a tag não for reconhecida
            TypeError: Se houver erro ao criar o widget
        """
        tag = elem.tag
        cls = self._get_class(tag)

        kwargs: Dict[str, Any] = {}
        field_id = None  # ID ou name do campo para armazenar referência
        
        # Processa atributos do elemento
        for k, v in elem.attrib.items():
            if k.startswith("on_"):
                # Eventos são processados depois
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
            # Erro mais informativo para problemas de tipo
            logger.error(f"Erro de tipo ao criar {tag}: {e}")
            logger.debug(f"kwargs: {kwargs}, children: {len(children)}")
            raise TypeError(f"Erro ao criar widget '{tag}': {e}. Verifique os parâmetros fornecidos.")
        except Exception as e:
            logger.error(f"Erro inesperado ao criar {tag}: {e}")
            raise

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

    def parse_xml_string(self, xml_string: str, handlers: Optional[Dict[str, Callable]] = None) -> List[Any]:
        """
        Converte uma string XML em widgets Flet.
        
        Args:
            xml_string: String XML contendo os widgets
            handlers: Dicionário de handlers de eventos (opcional)
        
        Returns:
            Lista de widgets Flet criados
        
        Raises:
            ET.ParseError: Se o XML estiver malformado
            ValueError: Se houver tags desconhecidas
        """
        try:
            # Envolve o XML em um elemento raiz para permitir múltiplos elementos no topo
            root = ET.fromstring(f"<root>{xml_string}</root>")
        except ET.ParseError as e:
            logger.error(f"Erro ao fazer parse do XML: {e}")
            raise ET.ParseError(f"XML malformado: {e}")
        
        widgets = []
        for child in root:
            if child.tag is ET.Comment:
                continue
            try:
                widget = self._instantiate_element(child, handlers or self.handlers)
                widgets.append(widget)
            except Exception as e:
                logger.error(f"Erro ao processar elemento '{child.tag}': {e}")
                raise
        
        return widgets
