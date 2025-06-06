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