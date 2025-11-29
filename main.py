import flet
from adapter import XMLFletAdapter
from handlers import Handlers

if __name__ == "__main__":
    handlers = Handlers()
    adapter = XMLFletAdapter(
        template_name="ui.xml.j2",
        handlers=handlers,
        title="Teste com Jinja",
        context={
            "nome": "Antonio"
        }
    )

    flet.app(target=adapter)
