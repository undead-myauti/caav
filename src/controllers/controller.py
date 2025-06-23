from src.models.main_model import Model
from src.views.main_view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(controller=self)
        self.selected_button = None

        self.navigation_map = {
            "inicio": "inicio",
            "informar_renda": "informar_renda",
            "adicionar_despesa": "adicionar_despesa",
            "atualizar_despesas": "atualizar_despesas",
            "atualizar_renda": "atualizar_renda"
        }

    def set_view(self, view):
        self.view = view

    def format_currency(self, valor: float) -> str:
        return f"{int(valor):,}".replace(",", ".")

    def handle_button_click(self, button):
        if self.selected_button:
            self.selected_button.configure(bg="white")
        button.configure(bg="#808080")
        self.selected_button = button

    def handle_get_expenses(self):
        return self.model.get_expenses()

    def register_expense(self, name, value):
        self.model.add_expense(
            {
                "name": name,
                "value": value
            }
        )
        self.view.renda_view.rebuild_initial_info()
        self.view.show_frame("inicio")

    def handle_navigation(self, action):
        if action in self.navigation_map:
            frame_to_show = self.navigation_map[action]
            self.view.show_frame(frame_to_show)

    def handle_update_renda_click(self, value):
        updated_income = self.model.update_income(value)
        self.view.renda_view.rebuild_initial_info()
        self.view.show_frame("inicio")

    def get_annual_income(self):
        return self.model.get_annual_income()

    def get_monthly_income(self):
        return self.model.get_monthly_income()

    def get_monthly_expenses(self):
        return self.model.get_monthly_expenses()

    def get_highest_expense(self):
        return self.model.get_highest_expense()

    def get_remaining_income(self):
        return self.model.get_remaining_income()  

    def run(self):
        self.view.main_loop()
