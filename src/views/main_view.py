import tkinter

class View:
    def __init__(self, controller):
        self.controller = controller

        self.root = tkinter.Tk()
        self.root.title("Financeiro turbinado")

        self.telas_container = tkinter.Frame(self.root, bg="#BDBDBD")
        self.telas_container.pack(fill='both', expand=True)
        self.create_frame_tela_renda(self.telas_container)
        self.frame_tela_renda.grid(row=0, column=0, sticky='nsew')

        # self.main_screen_container = tkinter.Frame(self.root, bg="#BDBDBD")
        # self.main_screen_container.pack(side=tkinter.RIGHT, fill='both', expand=True, padx=20, pady=20)

        # self.renda_screen(self.main_screen_container)
        # self.sidebar(self.sidebar_container)
        # self.topbar(self.topbar_container)

    def create_frame_tela_renda(self, container):
        self.frame_tela_renda = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_renda.grid(row=0, column=0, sticky='nsew')
        
        self.label_renda = tkinter.Label(self.frame_tela_renda, width=80, text="Informe a renda mensal", font=("Arial", 20), bg="#B1B1B1")
        self.entry_renda = tkinter.Entry(self.frame_tela_renda, width=80)
        self.button_enviar = tkinter.Button(self.frame_tela_renda, text="Enviar", font=("Arial", 20), bg="white")

        # Configurando o grid do frame
        self.frame_tela_renda.grid_columnconfigure(0, weight=1)
        self.frame_tela_renda.grid_rowconfigure(2, weight=1)

        # Posicionando os widgets usando grid
        self.label_renda.grid(row=0, column=0, pady=10, padx=10)
        self.entry_renda.grid(row=1, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=2, column=0, pady=10, padx=10)

    # def render_screen(self, container):
    #     self.create_frame()
    #     pass


    def sidebar(self, container):
        self.button_informar_renda = tkinter.Button(container, text="Informar renda")
        self.button_informar_renda.pack(pady=10, padx=10, fill='x')
        
        self.button_adicionar_despesa = tkinter.Button(container, text="Adicionar despesa")
        self.button_adicionar_despesa.pack(pady=10, padx=10, fill='x')

        self.button_atualizar_despesas = tkinter.Button(container, text="Atualizar despesas")
        self.button_atualizar_despesas.pack(pady=10, padx=10, fill='x')

        self.button_atualizar_renda = tkinter.Button(container, text="Atualizar renda")
        self.button_atualizar_renda.pack(pady=10, padx=10, fill='x')

    def topbar(self, container):
        self.label_financeiro_turbinado = tkinter.Label(container, text="Financeiro Turbinado", font=("Arial", 40), bg="#BDBDBD")
        self.label_financeiro_turbinado.pack(pady=10, padx=10, fill='x')

    def main_loop(self):
        self.root.mainloop()