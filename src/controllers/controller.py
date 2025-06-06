from src.models.main_model import Model
from src.views.main_view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(controller=self)
        
        # Mapeamento de ações para frames
        self.navigation_map = {
            "inicio": "inicio",
            "informar_renda": "informar_renda",
            "adicionar_despesa": "adicionar_despesa",
            "atualizar_despesas": "adicionar_despesa",  # Mesmo frame para adicionar e atualizar por enquanto
            "atualizar_renda": "atualizar_renda"
        }

    def handle_navigation(self, action):
        if action in self.navigation_map:
            frame_to_show = self.navigation_map[action]
            self.view.show_frame(frame_to_show)

    def run(self):
        self.view.main_loop()