from flet import app
import uuid
from adapter import XMLFletAdapter
from handlers import Handlers

if __name__ == "__main__":
    handlers = Handlers()

    adapter = XMLFletAdapter(
        template_name="ui.xml.j2",
        handlers=handlers,
        title="Teste com Jinja",
        context={
            "nome": "Antonio",
            "paises": [
                {"nome": "Brasil", "sigla": "br"},
                {"nome": "Estados Unidos", "sigla": "us"},
                {"nome": "Portugal", "sigla": "pt"},
                {"nome": "Argentina", "sigla": "ar"},
                {"nome": "Japão", "sigla": "jp"}
            ]
        }
    )

    app(target=adapter)
