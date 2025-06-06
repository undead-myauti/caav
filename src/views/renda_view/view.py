import tkinter

class RendaView:
    def __init__(self):
        self.frame_tela_renda = None
        
    def create_frame_tela_renda(self, main_view, container):
        self.frame_tela_renda = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_renda.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.label_renda = tkinter.Label(self.frame_tela_renda, width=80, text="Informe a renda mensal", font=("Arial", 20), bg="#B1B1B1")
        self.entry_renda = tkinter.Entry(self.frame_tela_renda, width=80)
        self.button_enviar = tkinter.Button(self.frame_tela_renda, text="Enviar", font=("Arial", 20), bg="white")

        self.frame_tela_renda.grid_columnconfigure(0, weight=1)
        self.frame_tela_renda.grid_rowconfigure(2, weight=1)

        self.label_renda.grid(row=0, column=0, pady=10, padx=10)
        self.entry_renda.grid(row=1, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=2, column=0, pady=10, padx=10)
        
        return self.frame_tela_renda
    
    def create_frame_update_renda(self, main_view, container):
        self.frame_tela_renda = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_renda.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.label_renda = tkinter.Label(self.frame_tela_renda, width=80, text="Informe o novo valor de renda mensal", font=("Arial", 20), bg="#B1B1B1")
        self.entry_renda = tkinter.Entry(self.frame_tela_renda, width=80)
        self.button_enviar = tkinter.Button(self.frame_tela_renda, text="Enviar", font=("Arial", 20), bg="white")   

        self.frame_tela_renda.grid_columnconfigure(0, weight=1)
        self.frame_tela_renda.grid_rowconfigure(2, weight=1)

        self.label_renda.grid(row=0, column=0, pady=10, padx=10)
        self.entry_renda.grid(row=1, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=2, column=0, pady=10, padx=10)
        
        return self.frame_tela_renda
    
    def create_frame_tela_principal(self, main_view, container):
        self.frame_tela_principal = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_principal.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.label_renda_anual = tkinter.Label(self.frame_tela_principal, text="Renda anual: ", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_renda_mensal = tkinter.Label(self.frame_tela_principal, text="Renda mensal: ", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_despesas_mensais = tkinter.Label(self.frame_tela_principal, text="Despesas mensais: ", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_maior_despesa_mensal = tkinter.Label(self.frame_tela_principal, text="Maior despesa mensal:", font=("Arial", 20), bg="#B1B1B1", anchor='w')
        self.label_saldo_liquido_mensal = tkinter.Label(self.frame_tela_principal, text="Saldo líquido mensal: ", font=("Arial", 20), bg="#B1B1B1", anchor='e')

        self.frame_tela_principal.grid_columnconfigure(0, weight=1)
        self.frame_tela_principal.grid_rowconfigure(2, weight=1)
        
        self.label_renda_anual.grid(row=0, column=0, pady=10, padx=10, sticky='ew')
        self.label_renda_mensal.grid(row=1, column=0, pady=10, padx=10, sticky='ew')
        self.label_despesas_mensais.grid(row=2, column=0, pady=10, padx=10, sticky='ew')
        self.label_maior_despesa_mensal.grid(row=3, column=0, pady=10, padx=10, sticky='ew')
        self.label_saldo_liquido_mensal.grid(row=4, column=0, pady=10, padx=10, sticky='e')
        return self.frame_tela_principal