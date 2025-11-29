import flet
import uuid
from adapter import XMLFletAdapter
from handlers import Handlers

if __name__ == "__main__":
    handlers = Handlers()
    
    # Define um ID único para a janela principal
    
    # adapter = XMLFletAdapter(
    #     template_name="ui.xml.j2",
    #     handlers=handlers,
    #     title="Teste com Jinja",
    #     context={
    #         "nome": "Antonio"
    #     }
    # )

    adapter = XMLFletAdapter(
        template_name="new.xml",
        title="Teste com Jinja",
    )
    
    # Cria uma função wrapper para registrar a janela
    def main_target(page: flet.Page):
        adapter(page)
    
    flet.app(target=main_target)
