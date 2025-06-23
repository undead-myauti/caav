import tkinter

class DespesaView:
    def __init__(self, controller=None):
        self.frame_tela_despesa = None
        self.controller = controller
        self.selected_expense = None


        self.expenses = self.controller.handle_get_expenses()
        self.expenses_map = {expense.name: expense.id for expense in self.expenses}

    def update_expenses(self):
        self.expenses = self.controller.handle_get_expenses()
        self.expenses_map = {expense.name: expense.id for expense in self.expenses}

    def create_frame_tela_despesa(self, main_view, container):
        self.frame_tela_despesa = tkinter.Frame(container, bg="#B1B1B1", name="frame_tela_despesa")
        self.frame_tela_despesa.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.label_despesa = tkinter.Label(self.frame_tela_despesa, width=80, text="Informe a despesa", font=("Arial", 20), bg="#B1B1B1")
        self.entry_despesa = tkinter.Entry(self.frame_tela_despesa, width=80)
        self.label_valor_despesa = tkinter.Label(self.frame_tela_despesa, width=80, text="Informe o valor da despesa", font=("Arial", 20), bg="#B1B1B1")
        self.entry_valor_despesa = tkinter.Entry(self.frame_tela_despesa, width=80)
        self.button_enviar = tkinter.Button(
            self.frame_tela_despesa, text="Enviar", 
            font=("Arial", 20), bg="white", 
            command=lambda: self.controller.register_expense(
                self.entry_despesa.get(), 
                self.entry_valor_despesa.get()
            )
        )

        self.frame_tela_despesa.grid_columnconfigure(0, weight=1)
        self.frame_tela_despesa.grid_rowconfigure(2, weight=1)

        self.label_despesa.grid(row=0, column=0, pady=10, padx=10)
        self.entry_despesa.grid(row=1, column=0, pady=10, padx=10)
        self.label_valor_despesa.grid(row=2, column=0, pady=10, padx=10)
        self.entry_valor_despesa.grid(row=3, column=0, pady=10, padx=10)
        self.button_enviar.grid(row=4, column=0, pady=10, padx=10)
        
        return self.frame_tela_despesa
    
    def create_frame_update_despesa(self, main_view, container):
        self.frame_tela_update_despesa = tkinter.Frame(container, bg="#B1B1B1", name="frame_tela_update_despesa")
        self.frame_tela_update_despesa.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        main_container = tkinter.Frame(self.frame_tela_update_despesa, bg="#B1B1B1", name="main_container")
        main_container.pack(fill='both', expand=True, padx=10, pady=10)

        buttons_frame = tkinter.Frame(main_container, bg="#B1B1B1", name="buttons_frame")
        buttons_frame.pack(fill='both', expand=True)

        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

        for i, expense in enumerate(self.expenses):
            row = i // 4
            col = i % 4
            
            button = tkinter.Button(
                buttons_frame, 
                text=expense.name,
                font=("Arial", 12),
                bg="white",
                relief="solid",
                width=15,
                name=f"{expense.id}"
            )
            button.configure(command=lambda b=button: self.controller.handle_button_click(b))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='ew')

        edit_frame = tkinter.Frame(self.frame_tela_update_despesa, bg="#B1B1B1", name="edit_frame")
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

        return self.frame_tela_update_despesa


    def create_frame_update_despesa_edit(self, main_view, container):
        self.frame_tela_update_despesa_edit = tkinter.Frame(container, bg="#B1B1B1", name="frame_tela_update_despesa_edit")
        self.frame_tela_update_despesa_edit.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.label_despesa_edit = tkinter.Label(self.frame_tela_update_despesa_edit, width=80, text="Informe o novo nome da despesa", font=("Arial", 20), bg="#B1B1B1")
        self.entry_despesa_edit = tkinter.Entry(self.frame_tela_update_despesa_edit, width=80)
        self.label_valor_despesa_edit = tkinter.Label(self.frame_tela_update_despesa_edit, width=80, text="Informe o novo valor da despesa", font=("Arial", 20), bg="#B1B1B1")
        self.entry_valor_despesa_edit = tkinter.Entry(self.frame_tela_update_despesa_edit, width=80)
        self.button_enviar_edit = tkinter.Button(self.frame_tela_update_despesa_edit, text="Atualizar", font=("Arial", 20), bg="white", command=lambda: self.controller.handle_update_expense(self.selected_expense, self.entry_despesa_edit.get(), self.entry_valor_despesa_edit.get()))

        if self.selected_expense:
            expense = self.controller.get_expense_by_id(self.selected_expense)
            self.entry_despesa_edit.insert(0, f"{expense.name}")
            self.entry_valor_despesa_edit.insert(0, f"{expense.value}")

        self.frame_tela_update_despesa_edit.grid_columnconfigure(0, weight=1)
        self.frame_tela_update_despesa_edit.grid_rowconfigure(2, weight=1)

        self.label_despesa_edit.grid(row=0, column=0, pady=10, padx=10)
        self.entry_despesa_edit.grid(row=1, column=0, pady=10, padx=10)
        self.label_valor_despesa_edit.grid(row=2, column=0, pady=10, padx=10)
        self.entry_valor_despesa_edit.grid(row=3, column=0, pady=10, padx=10)
        self.button_enviar_edit.grid(row=4, column=0, pady=10, padx=10)

        return self.frame_tela_update_despesa_edit
