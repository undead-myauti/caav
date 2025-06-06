import tkinter
from src.controllers.despesa_controller import DespesaController

class DespesaView:
    def __init__(self):
        self.frame_tela_despesa = None
        self.controller = DespesaController()
        self.controller.set_view(self)

        self.mock_despesa = [
            {
                "nome": "Aluguel",
                "valor": 1000
            }, 
            {
                "nome": "Giovana",
                "valor": 1000
            }, 
            {
                "nome": "Rafael",
                "valor": 1000
            },
            {
                "nome": "Rafael",
                "valor": 1000
            },
        ]
        
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
    
    def create_frame_update_despesa(self, main_view, container):
        self.frame_tela_despesa = tkinter.Frame(container, bg="#B1B1B1")
        self.frame_tela_despesa.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        main_container = tkinter.Frame(self.frame_tela_despesa, bg="#B1B1B1")
        main_container.pack(fill='both', expand=True, padx=10, pady=10)

        buttons_frame = tkinter.Frame(main_container, bg="#B1B1B1")
        buttons_frame.pack(fill='both', expand=True)

        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

        for i, despesa in enumerate(self.mock_despesa):
            row = i // 4
            col = i % 4
            
            button = tkinter.Button(
                buttons_frame, 
                text=despesa["nome"],
                font=("Arial", 12),
                bg="white",
                relief="solid",
                width=15
            )
            button.configure(command=lambda b=button: self.controller.handle_button_click(b))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='ew')

        edit_frame = tkinter.Frame(self.frame_tela_despesa, bg="#B1B1B1")
        edit_frame.pack(side='bottom', fill='x', pady=20)

        edit_button = tkinter.Button(
            edit_frame,
            text="Editar",
            font=("Arial", 12),
            bg="#ffb44a",
            relief="flat",
            width=10
        )
        edit_button.pack(pady=5)

        return self.frame_tela_despesa