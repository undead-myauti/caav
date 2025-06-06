class DespesaController:
    def __init__(self, view=None):
        self.view = view
        self.selected_button = None

    def set_view(self, view):
        self.view = view

    def handle_button_click(self, button):
        if self.selected_button:
            self.selected_button.configure(bg="white")  # Reseta cor do botão anterior
        button.configure(bg="#808080")  # Cinza escuro para indicar seleção
        self.selected_button = button 