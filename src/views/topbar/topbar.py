import tkinter

class Topbar:
    def __init__(self):
        self.label_financeiro_turbinado = None
        
    def create_topbar(self, main_view, container):
        container.grid_columnconfigure(0, weight=1)
        self.label_financeiro_turbinado = tkinter.Label(
            container,
            text="Financeiro Turbinado",
            font=("Arial", 24, "bold"),
            bg="#BDBDBD"
        )
        self.label_financeiro_turbinado.grid(row=0, column=0, pady=20) 