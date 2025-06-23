import tkinter

class RendaView:
    def __init__(self, controller):
        self.controller = controller
        self.frame_tela_renda = None

        self.monthly_income = self.controller.get_monthly_income()
        self.annual_income = self.controller.get_annual_income()
        self.monthly_expenses = self.controller.get_monthly_expenses()
        self.highest_expense = self.controller.get_highest_expense()
        self.remaining_income = self.controller.get_remaining_income()


    def rebuild_initial_info(self): 
        self.monthly_income = self.controller.get_monthly_income()
        self.annual_income = self.controller.get_annual_income()
        self.monthly_expenses = self.controller.get_monthly_expenses()
        self.highest_expense = self.controller.get_highest_expense()
        self.remaining_income = self.controller.get_remaining_income()
        
        if hasattr(self, 'frame_tela_principal'):
            self.update_principal_labels()
        elif hasattr(self, 'frame_tela_renda'):
            self.update_principal_labels()

    def update_principal_labels(self):
        self.label_renda_anual.configure(text=f"Renda anual: {self.annual_income}")
        self.label_renda_mensal.configure(text=f"Renda mensal: {self.monthly_income}")
        self.label_despesas_mensais.configure(text=f"Despesas mensais: {self.monthly_expenses}")
        self.label_maior_despesa_mensal.configure(text=f"Maior despesa mensal: {self.highest_expense}")
        self.label_saldo_liquido_mensal.configure(text=f"Saldo líquido mensal: {self.remaining_income}")

    def create_frame_tela_renda(self, main_view, container):
        self.frame_tela_renda = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_renda.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.label_renda = tkinter.Label(self.frame_tela_renda, width=80, text="Informe a renda mensal", font=("Arial", 20), bg="#B1B1B1")
        self.entry_renda_mensal = tkinter.Entry(self.frame_tela_renda, width=80)
        self.button_enviar = tkinter.Button(self.frame_tela_renda, text="Enviar", font=("Arial", 20), bg="white", command=lambda: self.controller.handle_update_renda_click(self.entry_renda_mensal.get()))

        self.frame_tela_renda.grid_columnconfigure(0, weight=1)
        self.frame_tela_renda.grid_rowconfigure(2, weight=1)

        self.label_renda.grid(row=0, column=0, pady=10, padx=10)
        self.entry_renda_mensal.grid(row=1, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=2, column=0, pady=10, padx=10)
        
        return self.frame_tela_renda

    def create_frame_update_renda(self, main_view, container):
        self.frame_tela_renda = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_renda.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.label_renda = tkinter.Label(self.frame_tela_renda, width=80, text="Informe o novo valor de renda mensal", font=("Arial", 20), bg="#B1B1B1")
        self.entry_renda = tkinter.Entry(self.frame_tela_renda, width=80)
        self.button_enviar = tkinter.Button(self.frame_tela_renda, text="Enviar", font=("Arial", 20), bg="white", command=lambda: self.controller.handle_update_renda_click(self.entry_renda.get()))   

        self.frame_tela_renda.grid_columnconfigure(0, weight=1)
        self.frame_tela_renda.grid_rowconfigure(2, weight=1)

        self.label_renda.grid(row=0, column=0, pady=10, padx=10)
        self.entry_renda.grid(row=1, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=2, column=0, pady=10, padx=10)
        
        return self.frame_tela_renda

    def create_frame_tela_principal(self, main_view, container):
        self.frame_tela_principal = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_principal.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.label_renda_anual = tkinter.Label(self.frame_tela_principal, text=f"Renda anual: R$ {self.controller.format_currency(self.annual_income)}", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_renda_mensal = tkinter.Label(self.frame_tela_principal, text=f"Renda mensal: R$ {self.controller.format_currency(self.monthly_income)}", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_despesas_mensais = tkinter.Label(self.frame_tela_principal, text=f"Despesas mensais: R$ {self.controller.format_currency(self.monthly_expenses)}", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_maior_despesa_mensal = tkinter.Label(self.frame_tela_principal, text=f"Maior despesa mensal: R$ {self.controller.format_currency(self.highest_expense)}", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_saldo_liquido_mensal = tkinter.Label(self.frame_tela_principal, text=f"Saldo líquido mensal: R$ {self.controller.format_currency(self.remaining_income)}", font=("Arial", 20), bg="#B1B1B1", anchor='e')

        self.frame_tela_principal.grid_columnconfigure(0, weight=1)
        self.frame_tela_principal.grid_rowconfigure(2, weight=1)

        self.label_renda_anual.grid(row=0, column=0, pady=10, padx=10, sticky='ew')
        self.label_renda_mensal.grid(row=1, column=0, pady=10, padx=10, sticky='ew')
        self.label_despesas_mensais.grid(row=2, column=0, pady=10, padx=10, sticky='ew')
        self.label_maior_despesa_mensal.grid(row=3, column=0, pady=10, padx=10, sticky='ew')
        self.label_saldo_liquido_mensal.grid(row=4, column=0, pady=10, padx=10, sticky='e')
        return self.frame_tela_principal
