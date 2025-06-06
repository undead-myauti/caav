import tkinter

class Sidebar:
    def __init__(self):
        self.button_informar_renda = None
        self.button_adicionar_despesa = None
        self.button_atualizar_despesas = None
        self.button_atualizar_renda = None
        
    def create_sidebar(self, container, commands):
        self.button_inicio = tkinter.Button(container, text="Início", command=commands["Início"])
        self.button_inicio.pack(pady=10, padx=10, fill='x')

        self.button_informar_renda = tkinter.Button(container, text="Informar renda", command=commands["Informar renda"])
        self.button_informar_renda.pack(pady=10, padx=10, fill='x')
        
        self.button_adicionar_despesa = tkinter.Button(container, text="Adicionar despesa", command=commands["Adicionar despesa"])
        self.button_adicionar_despesa.pack(pady=10, padx=10, fill='x')

        self.button_atualizar_despesas = tkinter.Button(container, text="Atualizar despesas", command=commands["Atualizar despesas"])
        self.button_atualizar_despesas.pack(pady=10, padx=10, fill='x')

        self.button_atualizar_renda = tkinter.Button(container, text="Atualizar renda", command=commands["Atualizar renda"])
        self.button_atualizar_renda.pack(pady=10, padx=10, fill='x') 