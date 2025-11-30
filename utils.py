import xml.etree.ElementTree as ET
from typing import Any, Dict

from flet.core.page import ControlEvent

from adapter import XMLFletAdapter

def xml_to_dict(xml_input: str) -> Dict[str, Any]:
    """
    Converte uma string XML em um dicionário Python.
    
    Args:
        xml_input (str): XML como string.
    
    Returns:
        dict: Representação em dicionário do XML.
    """

    def _element_to_dict(element: ET.Element) -> Dict[str, Any]:
        node = {}
        # Adiciona atributos
        if element.attrib:
            node.update({f"@{k}": v for k, v in element.attrib.items()})
        # Adiciona filhos
        children = list(element)
        if children:
            child_dict = {}
            for child in children:
                child_name = child.tag
                child_data = _element_to_dict(child)
                if child_name in child_dict:
                    # Se já existe, transforma em lista
                    if not isinstance(child_dict[child_name], list):
                        child_dict[child_name] = [child_dict[child_name]]
                    child_dict[child_name].append(child_data)
                else:
                    child_dict[child_name] = child_data
            node.update(child_dict)
        # Adiciona texto, se houver
        text = (element.text or "").strip()
        if text and (children or element.attrib):
            node["#text"] = text
        elif text:
            return text
        return node

    root = ET.fromstring(xml_input)
    return {root.tag: _element_to_dict(root)}
