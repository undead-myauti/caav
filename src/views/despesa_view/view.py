import tkinter

class DespesaView:
    def __init__(self):
        self.frame_tela_despesa = None
        
    def create_frame_tela_despesa(self, main_view, container):
        self.frame_tela_despesa = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_despesa.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.label_despesa = tkinter.Label(self.frame_tela_despesa, width=80, text="Informe a despesa", font=("Arial", 20), bg="#B1B1B1")
        self.entry_despesa = tkinter.Entry(self.frame_tela_despesa, width=80)
        self.label_valor_despesa = tkinter.Label(self.frame_tela_despesa, width=80, text="Informe o valor da despesa", font=("Arial", 20), bg="#B1B1B1")
        self.entry_valor_despesa = tkinter.Entry(self.frame_tela_despesa, width=80)
        self.button_enviar = tkinter.Button(self.frame_tela_despesa, text="Enviar", font=("Arial", 20), bg="white")

        self.frame_tela_despesa.grid_columnconfigure(0, weight=1)
        self.frame_tela_despesa.grid_rowconfigure(2, weight=1)

        self.label_despesa.grid(row=0, column=0, pady=10, padx=10)
        self.entry_despesa.grid(row=1, column=0, pady=10, padx=10)
        self.label_valor_despesa.grid(row=2, column=0, pady=10, padx=10)
        self.entry_valor_despesa.grid(row=3, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=4, column=0, pady=10, padx=10)
        
        return self.frame_tela_despesa