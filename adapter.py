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
        """
        self.template_name = template_name
        self.handlers = handlers
        self.title = title
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.context = context

    def __call__(self, page: Page):
        page.title = self.title

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

    def _instantiate_element(self, elem: ET.Element, handlers: Optional[Dict[str, Callable]] = None):
        tag = elem.tag
        cls = self._get_class(tag)

        kwargs: Dict[str, Any] = {}
        for k, v in elem.attrib.items():
            if k.startswith("on_"):
                kwargs[k] = v
                continue
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

        for ev_name, ev_val in event_attrs.items():
            handler = handlers.get(ev_val) if handlers else None
            if handler:
                self._bind_event(instance, ev_name, handler)

        return instance

    def parse_xml_string(self, xml_string: str, handlers: Optional[Dict[str, Callable]] = None):
        root = ET.fromstring(f"<root>{xml_string}</root>")
        widgets = []
        for child in root:
            widgets.append(self._instantiate_element(child, handlers))
        return widgets
