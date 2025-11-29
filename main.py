import sys

import flet  # type: ignore

from adapter import XMLFletAdapter

if __name__ == "__main__":

    def on_submit(e: flet.ControlEvent, field_data: dict = None):
        """
        Callback que recebe os dados dos campos automaticamente.
        O adapter detecta se a função aceita 2 parâmetros e passa os dados.
        """
        if field_data:
            print("=== Dados do Formulário ===")
            for field_id, value in field_data.items():
                print(f"{field_id}: {value}")
            print("=" * 30)
            
            # Exemplo: validar campos específicos
            if not field_data.get('nome'):
                print("⚠️  Nome é obrigatório!")
            if not field_data.get('email'):
                print("⚠️  E-mail é obrigatório!")
            if not field_data.get('termos'):
                print("⚠️  Você deve aceitar os termos!")
        else:
            print("Botão Cadastrar clicado!")

    def on_clear(e: flet.ControlEvent, field_data: dict = None):
        """Limpa os campos do formulário"""
        # Acessa o adapter através da página
        adapter = None
        if hasattr(e.control.page, 'data') and isinstance(e.control.page.data, dict):
            adapter = e.control.page.data.get('adapter')
        if adapter and hasattr(adapter, 'fields'):
            # Limpa os campos
            if 'nome' in adapter.fields:
                adapter.fields['nome'].value = ""
                adapter.fields['nome'].update()
            if 'email' in adapter.fields:
                adapter.fields['email'].value = ""
                adapter.fields['email'].update()
            if 'senha' in adapter.fields:
                adapter.fields['senha'].value = ""
                adapter.fields['senha'].update()
            if 'pais' in adapter.fields:
                adapter.fields['pais'].value = None
                adapter.fields['pais'].update()
            if 'termos' in adapter.fields:
                adapter.fields['termos'].value = False
                adapter.fields['termos'].update()
            print("Campos limpos!")

    def on_exit(e: flet.ControlEvent):
        print("Sair clicado; você pode chamar page.window_close() ou semelhante")
        sys.exit(0)

    handlers = {
        "on_submit": on_submit, 
        "on_clear": on_clear,
        "on_exit": on_exit
    }

    adapter = XMLFletAdapter(
        template_name="ui.xml.j2",
        handlers=handlers,
        title="Teste com Jinja",
        context={
            "nome": "Antonio"
        }
    )

    flet.app(target=adapter)
