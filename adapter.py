import ast
from contextlib import suppress
import inspect
import logging
import uuid
import xml.etree.ElementTree as ET
from typing import Any, Callable, Dict, List, Optional, Union

import flet
from jinja2 import Environment, FileSystemLoader
from factories import FACTORY_MAPPER
from window_manager import get_window_manager

logger = logging.getLogger(__name__)

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

    def __init__(
        self,
        template_name: str,
        title: str,
        templates_dir: str = "templates",
        context: Optional[Dict[str, Any]] = None,
        handlers: Union[Dict[str, Callable], Any] = {},
    ):

        if not template_name:
            raise ValueError("template_name não pode estar vazio")
        
        print(f"Renderizando {template_name}")
        
        self.main_window_id = f"main_{uuid.uuid4().hex[:8]}"
        self.template_name = template_name
        self.handlers = handlers
        self.title = title
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.context = context or {}
        self.fields: Dict[str, Any] = {}
        self.page: Optional[flet.Page] = None
        self.window_manager = get_window_manager()
        self.window_id: Optional[str] = None


    def render_template(self, name, **context):
        template = self.env.get_template(name)
        return template.render(context)

    def __call__(self, page: flet.Page) -> None:
        self.page = page
        page.title = self.title
        self.fields.clear()
        
        if not hasattr(page, 'data') or page.data is None or not isinstance(page.data, dict):
            page.data = {}

        page.adapter = self
        # page.data['adapter'] = self
        page.data['window_manager'] = self.window_manager
        
        if self.window_id:
            self.window_manager.register_window(self.window_id, page, self)

        xml_string = self.render_template(self.template_name, **self.context)

        widgets = self.parse_xml_string(xml_string, handlers=self.handlers)
        for w in widgets:
            page.add(w)
        logger.info(f"Interface carregada: {len(self.fields)} campos registrados")


    def _parse_attr_value(self, val: str) -> Any:
        if val is None:
            return None
        
        s = val.strip()
        if s == "":
            return ""
        
        if s.lower() in ("true", "false"):
            return s.lower() == "true"
        
        if s.lower() in ("none", "null"):
            return None
        
        try:
            if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
                return int(s)
        except ValueError:
            pass
        
        try:
            return float(s)
        except ValueError:
            pass
        
        if s.startswith("#") and len(s) in (7, 9) and all(c in "0123456789abcdefABCDEF" for c in s[1:]):
            return s
        
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            pass
        
        return s

    def _get_handler(
        self,
        handler_name: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None
    ) -> Optional[Callable]:

        if handlers is None:
            handlers = self.handlers
        
        if handlers is None:
            return None
        
        if isinstance(handlers, dict):
            return handlers.get(handler_name)
        
        if hasattr(handlers, handler_name):
            handler = getattr(handlers, handler_name)
            if callable(handler):
                return handler
        
        return None

    def _bind_event(self, obj: Any, event_name: str, handler: Callable) -> bool:
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
        if field is None:
            return None
        
        if hasattr(field, 'value'):
            return field.value
        elif hasattr(field, 'text'):
            return field.text
        elif hasattr(field, 'data'):
            return field.data
        elif hasattr(field, 'selected_index'):
            return field.selected_index
        
        logger.warning(f"Campo {type(field).__name__} não possui atributo de valor conhecido")
        return None

    def get_field_data(self, field_ids: Optional[List[str]] = None) -> Dict[str, Any]:
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
        return self.fields.get(field_id)
    
    def set_field_value(self, field_id: str, value: Any) -> bool:
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
        if field_ids is None:
            field_ids = list(self.fields.keys())
        
        cleared = 0
        for field_id in field_ids:
            field = self.get_field(field_id)
            if field is None:
                continue
            
            try:
                if hasattr(field, 'value'):
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
        if not self.page:
            return
        
        for field in self.fields.values():
            try:
                field.update()
            except Exception as e:
                logger.error(f"Erro ao atualizar campo: {e}")
    
    def rerender(self, context):
        print('renderizando dnv')
        return self.navigate_to(
            template_name=self.template_name,
            handlers=self.handlers,
            title=self.title,
            context={**self.context, **context}
        )
    
    def navigate_to(
        self,
        template_name: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None,
        title: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> bool:
        if not self.page:
            logger.error("Não é possível navegar: página não inicializada")
            return False

        self.page.clean()
        self.fields.clear()

        if title:
            self.page.title = title
            self.title = title
        
        if handlers:
            self.handlers = handlers
        
        if context:
            self.context = {**self.context, **context}

        self.template_name = template_name
        xml_string = self.render_template(template_name, **self.context)
        logger.debug(f"Navegando para template '{template_name}'")

        try:
            widgets = self.parse_xml_string(xml_string, handlers=self.handlers)
            for w in widgets:
                self.page.add(w)
            return True
        except Exception as e:
            logger.error(f"Erro ao processar XML do template '{template_name}': {e}")
            return False

    def open_window(
        self,
        template_name: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None,
        title: str = "Nova Janela",
        context: Optional[Dict[str, Any]] = None,
        window_id: Optional[str] = None,
        width: int = 800,
        height: int = 600,
    ) -> Optional[str]:

        if handlers is None:
            handlers = self.handlers
        
        return self.window_manager.open_new_window(
            template_name=template_name,
            handlers=handlers,
            title=title,
            context=context,
            window_id=window_id,
            width=width,
            height=height,
            templates_dir=(
                self.env.loader.searchpath[0]
                if hasattr(self.env.loader, 'searchpath')
                else "templates"
            )
        )
    
    def replace_current_window(
        self,
        template_name: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None,
        title: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> bool:

        if not self.page:
            logger.error("Não é possível substituir janela: página não inicializada")
            return False
        
        if self.window_id:
            return self.window_manager.replace_window(
                window_id=self.window_id,
                template_name=template_name,
                handlers=handlers or self.handlers,
                title=title,
                context=context
            )

        else:
            return self.navigate_to(
                template_name=template_name,
                handlers=handlers,
                title=title,
                context=context
            ) is not None

    def close_current_window(self) -> bool:
        if not self.page:
            return False
        
        if self.window_id:
            return self.window_manager.close_window(self.window_id)
        else:
            try:
                self.page.window.close()
                return True
            except Exception as e:
                logger.error(f"Erro ao fechar janela: {e}")
                return False

    def _create_callback_wrapper(self, original_handler: Callable) -> Callable:
        def wrapper(e: flet.ControlEvent):
            sig = inspect.signature(original_handler)
            params = list[str](sig.parameters.keys())
            if len(params) == 2:
                field_data = self.get_field_data()
                return original_handler(e, field_data)
            if len(params) == 1:
                return original_handler(e)
            if len(params) == 0:
                return original_handler()
            raise ValueError('Número de parametros inválido')

        return wrapper

    def _get_class(self, tag: str) -> Optional[type]:
        cls = getattr(flet, tag, None)
        if cls is not None:
            return cls
        
        if "." in tag:
            mod, name = tag.split(".", 1)
            submodule = getattr(flet, mod, None)
            if submodule:
                cls = getattr(submodule, name, None)
                if cls is not None:
                    return cls

        return None

    def _instantiate_element(
        self,
        elem: ET.Element,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None
    ) -> Any:
        tag = elem.tag

        kwargs: Dict[str, Any] = {}
        field_id = None
        for key, value in elem.attrib.items():
            if key.startswith("on_"):
                kwargs[key] = value
                continue

            if key in ("id", "name") and tag in FIELD_TYPES:
                field_id = value
                continue

            kwargs[key] = self._parse_attr_value(value)

        children = []
        text_content = (elem.text or "").strip()
        for child in elem:
            if child.tag is ET.Comment:
                continue

            c = self._instantiate_element(child, handlers)
            children.append(c)

        event_attrs = {k: v for k, v in kwargs.items() if k.startswith("on_")}
        for k in list(kwargs.keys()):
            if k.startswith("on_"):
                del kwargs[k]

        sig = None
        with suppress(ValueError, TypeError):
            cls = self._get_class(tag)
            sig = inspect.signature(cls)

        if children:
            if "controls" in (sig.parameters if sig else {}):
                kwargs["controls"] = children
            elif "content" in (sig.parameters if sig else {}):
                kwargs["content"] = (
                    children[0]
                    if len(children) == 1
                    else flet.Column(controls=children)
                )

            elif tag in CHILD_ATTRS:
                kwargs[CHILD_ATTRS[tag]] = children

        if text_content:
            if "text" in (sig.parameters if sig else {}):
                kwargs.setdefault("text", text_content)
            elif "value" in (sig.parameters if sig else {}):
                kwargs.setdefault("value", text_content)

        factory = FACTORY_MAPPER[tag]
        instance = factory(kwargs)
        if field_id:
            self.fields[field_id] = instance

        for event_name, ev_value in event_attrs.items():
            handler_method = self._get_handler(ev_value, handlers)
            if handler_method:
                wrapped_handler = self._create_callback_wrapper(handler_method)
                self._bind_event(instance, event_name, wrapped_handler)

        return instance


    def parse_xml_string(
        self,
        xml_string: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None
    ) -> List[Any]:

        try:
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
