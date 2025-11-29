import logging
import multiprocessing
import sys
from typing import Dict, Optional, Any, Callable, Union
import flet
from flet import Page

logger = logging.getLogger(__name__)


def _create_window_process(
    template_name: str,
    title: str,
    templates_dir: str,
    context: Dict[str, Any],
    window_id: str,
    width: int,
    height: int,
    handlers_module: Optional[str] = None,
    handlers_class: Optional[str] = None,
):
    """
    Função auxiliar para criar uma janela em um processo separado.
    Esta função é serializável para multiprocessing.
    """
    from adapter import XMLFletAdapter
    
    # Recria os handlers se necessário
    handlers = None
    if handlers_module and handlers_class and handlers_module != "__main__":
        try:
            import importlib
            module = importlib.import_module(handlers_module)
            handlers = getattr(module, handlers_class)()
            logger.info(f"Handlers recriados: {handlers_module}.{handlers_class}")
        except Exception as e:
            logger.warning(f"Erro ao recriar handlers: {e}. Continuando sem handlers.")
    elif handlers_module == "__main__":
        logger.warning("Handlers do módulo __main__ não podem ser recriados em processo separado. Continuando sem handlers.")
    
    def create_window(page: Page):
        """Função callback para criar a janela."""
        # Configura o tamanho e título da janela
        page.window.width = width
        page.window.height = height
        page.title = title
        
        adapter = XMLFletAdapter(
            template_name=template_name,
            handlers=handlers,
            title=title,
            templates_dir=templates_dir,
            context=context or {}
        )
        
        # Obtém o window_manager global (cada processo tem sua própria instância)
        from window_manager import get_window_manager
        window_manager = get_window_manager()
        adapter.window_manager = window_manager
        adapter.window_id = window_id
        
        # Chama o adapter para inicializar a página
        adapter(page)
        
        # Registra a janela no gerenciador
        window_manager.register_window(window_id, page, adapter)
    
    try:
        flet.app(
            target=create_window,
            view=flet.AppView.FLET_APP
        )
    except Exception as e:
        logger.error(f"Erro ao executar app em processo: {e}")


class WindowManager:
    """
    Gerenciador de múltiplas janelas para aplicações Flet.
    
    Permite criar, substituir e gerenciar múltiplas janelas de forma centralizada.
    """
    
    def __init__(self):
        """Inicializa o gerenciador de janelas."""
        self.windows: Dict[str, Page] = {}  # Dicionário de janelas por ID
        self.window_adapters: Dict[str, Any] = {}  # Adapters associados a cada janela
        self.main_window_id: Optional[str] = None
        # Nota: Não usamos lock porque cada processo tem seu próprio window_manager
    
    def register_window(self, window_id: str, page: Page, adapter: Any) -> None:
        """
        Registra uma janela no gerenciador.
        
        Args:
            window_id: Identificador único da janela
            page: Instância da página Flet
            adapter: Adapter associado à janela
        """
        self.windows[window_id] = page
        self.window_adapters[window_id] = adapter
        if self.main_window_id is None:
            self.main_window_id = window_id

        logger.info(f"Janela '{window_id}' registrada")
    
    def get_window(self, window_id: str) -> Optional[Page]:
        """
        Obtém uma janela pelo ID.
        
        Args:
            window_id: Identificador da janela
            
        Returns:
            Instância da página ou None se não encontrada
        """
        return self.windows.get(window_id)
    
    def get_adapter(self, window_id: str) -> Optional[Any]:
        """
        Obtém o adapter associado a uma janela.
        
        Args:
            window_id: Identificador da janela
            
        Returns:
            Adapter ou None se não encontrado
        """
        return self.window_adapters.get(window_id)
    
    def close_window(self, window_id: str) -> bool:
        """
        Fecha uma janela específica.
        
        Args:
            window_id: Identificador da janela
            
        Returns:
            True se a janela foi fechada, False caso contrário
        """
        if window_id in self.windows:
            page = self.windows[window_id]
            try:
                page.window.close()
                del self.windows[window_id]
                if window_id in self.window_adapters:
                    del self.window_adapters[window_id]
                if self.main_window_id == window_id:
                    self.main_window_id = None
                    # Define a primeira janela restante como principal
                    if self.windows:
                        self.main_window_id = next(iter(self.windows.keys()))
                logger.info(f"Janela '{window_id}' fechada")
                return True
            except Exception as e:
                logger.error(f"Erro ao fechar janela '{window_id}': {e}")
                return False
        return False
    
    def replace_window(
        self,
        window_id: str,
        template_name: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None,
        title: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> bool:
        """
        Substitui o conteúdo de uma janela existente por um novo template.
        
        Args:
            window_id: Identificador da janela a ser substituída
            template_name: Nome do novo template
            handlers: Handlers para o novo template
            title: Título da janela (opcional)
            context: Contexto para o template (opcional)
            
        Returns:
            True se a substituição foi bem-sucedida, False caso contrário
        """
        adapter = self.get_adapter(window_id)
        if not adapter:
            logger.error(f"Adapter não encontrado para janela '{window_id}'")
            return False
        
        try:
            adapter.navigate_to(
                template_name=template_name,
                handlers=handlers,
                title=title,
                context=context
            )
            logger.info(f"Janela '{window_id}' substituída por template '{template_name}'")
            return True
        except Exception as e:
            logger.error(f"Erro ao substituir janela '{window_id}': {e}")
            return False
    
    def open_new_window(
        self,
        template_name: str,
        handlers: Optional[Union[Dict[str, Callable], Any]] = None,
        title: str = "Nova Janela",
        context: Optional[Dict[str, Any]] = None,
        window_id: Optional[str] = None,
        width: int = 800,
        height: int = 600,
        templates_dir: str = "templates",
    ) -> Optional[str]:
        """
        Abre uma nova janela com um template.
        
        Args:
            template_name: Nome do template a ser carregado
            handlers: Handlers para a nova janela (deve ser uma classe ou None)
            title: Título da nova janela
            context: Contexto para o template
            window_id: ID único para a janela (gerado automaticamente se None)
            width: Largura da janela
            height: Altura da janela
            templates_dir: Diretório dos templates
            
        Returns:
            ID da janela criada ou None em caso de erro
        """
        if window_id is None:
            import uuid
            window_id = f"window_{uuid.uuid4().hex[:8]}"
        
        # Tenta obter informações sobre a classe de handlers para recriá-la no processo filho
        handlers_module = None
        handlers_class = None
        if handlers is not None and not isinstance(handlers, dict):
            # Se handlers é uma instância de classe, tenta obter o nome da classe e módulo
            handlers_class = handlers.__class__.__name__
            handlers_module = handlers.__class__.__module__
            # Se o módulo for __main__, isso pode não funcionar bem com multiprocessing
            if handlers_module == "__main__":
                logger.warning("Handlers do módulo __main__ podem não funcionar com multiprocessing")
        
        try:
            # Cria um novo processo para a janela
            # Cada processo tem sua própria thread principal, permitindo que o Flet funcione
            process = multiprocessing.Process(
                target=_create_window_process,
                args=(
                    template_name,
                    title,
                    templates_dir,
                    context or {},
                    window_id,
                    width,
                    height,
                    handlers_module,
                    handlers_class,
                ),
                daemon=False
            )
            process.start()
            logger.info(f"Nova janela '{window_id}' criada com template '{template_name}' em processo separado")
            return window_id
        except Exception as e:
            logger.error(f"Erro ao criar nova janela: {e}")
            return None
    
    def list_windows(self) -> list[str]:
        """
        Lista todos os IDs das janelas abertas.
        
        Returns:
            Lista de IDs das janelas
        """
        return list(self.windows.keys())
    
    def get_main_window(self) -> Optional[Page]:
        """
        Obtém a janela principal.
        
        Returns:
            Instância da página principal ou None
        """
        if self.main_window_id:
            return self.windows.get(self.main_window_id)
        return None


# Instância global do gerenciador
_global_window_manager: Optional[WindowManager] = None


def get_window_manager() -> WindowManager:
    """
    Obtém a instância global do gerenciador de janelas.
    
    Returns:
        Instância do WindowManager
    """
    global _global_window_manager
    if _global_window_manager is None:
        _global_window_manager = WindowManager()
    return _global_window_manager

