from flet import ControlEvent, Page

class Handlers:
    def on_rerender(self, e: ControlEvent, field_data: dict = None):
        context = {
            "paises": [
                {"nome": "Brasil", "sigla": "br"},
                {"nome": "Estados Unidos", "sigla": "us"},
                {"nome": "Portugal", "sigla": "pt"},
                {"nome": "Argentina", "sigla": "ar"},
                {"nome": "Japão", "sigla": "jp"}
            ]
        }
        e.page.adapter.rerender(context)

    def on_submit(self, e: ControlEvent, field_data: dict = None):
        if not field_data:
            print("⚠️  Nenhum dado recebido!")
            return

        errors = []
        if not field_data.get('nome') or not str(field_data.get('nome', '')).strip():
            errors.append("Nome é obrigatório!")
        if not field_data.get('email') or not str(field_data.get('email', '')).strip():
            errors.append("E-mail é obrigatório!")
        if not field_data.get('termos'):
            errors.append("Você deve aceitar os termos de uso!")

        if errors:
            print("⚠️  Erros de validação:")
            for error in errors:
                print(f"  - {error}")
            return

        print("=== Cadastro realizado com sucesso! ===")
        for field_id, value in field_data.items():
            print(f"{field_id}: {value}")
        print("=" * 30)


        pais_nome = None
        if field_data.get('pais'):
            paises_map = {
                "br": "Brasil",
                "us": "Estados Unidos",
                "pt": "Portugal",
                "ar": "Argentina",
                "jp": "Japão"
            }
            pais_nome = paises_map.get(field_data['pais'], field_data['pais'])
        
        success_context = {
            "nome": field_data.get('nome', ''),
            "dados": {
                "nome": field_data.get('nome', ''),
                "email": field_data.get('email', ''),
                "pais": pais_nome
            }
        }
        
        e.page.adapter.navigate_to(
            template_name="success.xml.j2",
            title="Cadastro Realizado",
            context=success_context
        )


    def on_clear(self, e: ControlEvent, field_data: dict = None):
        cleared = e.page.adapter.clear_fields()
        print(f"✅ {cleared} campo(s) limpo(s)!")


    def on_exit(self, e: ControlEvent):
        e.control.page.window.close()

    def on_back(self, e: ControlEvent):
        e.page.adapter.navigate_to(
            template_name="ui.xml.j2",
            title="Teste com Jinja",
            context={"nome": "Antonio"}
        )

    
    def on_open_new_window(self, e: ControlEvent, field_data: dict = None):
        context = {
            "nome": field_data.get('nome', 'Visitante') if field_data else "Visitante",
            "dados": {
                "nome": field_data.get('nome', '') if field_data else '',
                "email": field_data.get('email', '') if field_data else '',
            }
        }
        
        window_id = e.page.adapter.open_window(
            template_name="success.xml.j2",
            title="Nova Janela - Sucesso",
            context=context,
            width=600,
            height=500
        )
        
        if window_id:
            print(f"✅ Nova janela '{window_id}' aberta!")
        else:
            print("⚠️  Erro ao abrir nova janela!")

    
    def on_replace_window(self, e: ControlEvent, field_data: dict = None):
        context = {
            "nome": field_data.get('nome', 'Visitante') if field_data else "Visitante",
            "dados": {
                "nome": field_data.get('nome', '') if field_data else '',
                "email": field_data.get('email', '') if field_data else '',
            }
        }
        
        success = e.page.adapter.replace_current_window(
            template_name="success.xml.j2",
            title="Janela Substituída - Sucesso",
            context=context
        )
        
        if success:
            print("✅ Janela atual substituída!")
        else:
            print("⚠️  Erro ao substituir janela!")
