import flet  # type: ignore

class Handlers:
    def on_submit(self, e: flet.ControlEvent, field_data: dict = None):
        """
        Callback que recebe os dados dos campos automaticamente.
        Valida os dados e navega para a página de sucesso se tudo estiver correto.
        """
        if not field_data:
            print("⚠️  Nenhum dado recebido!")
            return

        # Validação dos campos
        errors = []
        if not field_data.get('nome') or not str(field_data.get('nome', '')).strip():
            errors.append("Nome é obrigatório!")
        if not field_data.get('email') or not str(field_data.get('email', '')).strip():
            errors.append("E-mail é obrigatório!")
        if not field_data.get('termos'):
            errors.append("Você deve aceitar os termos de uso!")

        # Se houver erros, exibe e não prossegue
        if errors:
            print("⚠️  Erros de validação:")
            for error in errors:
                print(f"  - {error}")
            return

        # Cadastro válido - navega para página de sucesso
        print("=== Cadastro realizado com sucesso! ===")
        for field_id, value in field_data.items():
            print(f"{field_id}: {value}")
        print("=" * 30)

        # Acessa o adapter através da página
        adapter = None
        if hasattr(e.control.page, 'data') and isinstance(e.control.page.data, dict):
            adapter = e.control.page.data.get('adapter')
        
        if adapter:
            # Prepara os dados para a página de sucesso
            # Mapeia o país se existir
            pais_nome = None
            if field_data.get('pais'):
                # Se for uma sigla, tenta encontrar o nome
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
            
            # Navega para a página de sucesso
            adapter.navigate_to(
                template_name="success.xml.j2",
                title="Cadastro Realizado",
                context=success_context
            )
        else:
            print("⚠️  Erro: adapter não encontrado!")

    def on_clear(self, e: flet.ControlEvent, field_data: dict = None):
        """Limpa os campos do formulário"""
        # Acessa o adapter através da página
        adapter = None
        if hasattr(e.control.page, 'data') and isinstance(e.control.page.data, dict):
            adapter = e.control.page.data.get('adapter')
        
        if adapter:
            # Usa o método utilitário do adapter
            cleared = adapter.clear_fields()
            print(f"✅ {cleared} campo(s) limpo(s)!")
        else:
            print("⚠️  Erro: adapter não encontrado!")

    def on_exit(self, e: flet.ControlEvent):
        page: flet.Page = e.control.page
        page.window.close()

    def on_back(self, e: flet.ControlEvent):
        """Volta para a página inicial de cadastro"""
        adapter = None
        if hasattr(e.control.page, 'data') and isinstance(e.control.page.data, dict):
            adapter = e.control.page.data.get('adapter')
        
        if adapter:
            adapter.navigate_to(
                template_name="ui.xml.j2",
                title="Teste com Jinja",
                context={"nome": "Antonio"}
            )
        else:
            print("⚠️  Erro: adapter não encontrado!")
