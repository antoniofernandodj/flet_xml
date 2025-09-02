import sys

import flet  # type: ignore

from adapter import XMLFletAdapter

if __name__ == "__main__":

    def on_botaoclick(e: flet.ControlEvent):
        print("Botão clicado! evento:", e)

    def on_exit(e: flet.ControlEvent):
        print("Sair clicado; você pode chamar page.window_close() ou semelhante")
        sys.exit(0)

    handlers = {"on_botaoclick": on_botaoclick, 'on_exit': on_exit}

    flet.app(
        target=XMLFletAdapter(
            template_name="ui.xml.j2",
            handlers=handlers,
            title="Teste com Jinja",
            context={
                "nome": "Antonio"
            }
        ),
    )
