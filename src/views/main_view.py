import tkinter
from src.views.renda_view.view import RendaView
from src.views.despesa_view.view import DespesaView
from src.views.sidebar.sidebar import Sidebar
from src.views.topbar.topbar import Topbar

class View:
    def __init__(self, controller):
        self.controller = controller
        self.renda_view = RendaView()
        self.despesa_view = DespesaView(controller=controller)
        self.sidebar = Sidebar()
        self.topbar = Topbar()
        self.frames = {}

        self.root = tkinter.Tk()
        self.root.title("Financeiro turbinado")
        self.root.geometry("1000x600")

        ###### Topbar ######
        self.topbar_container = tkinter.Frame(self.root, bg="#BDBDBD", height=80)
        self.topbar_container.pack(side=tkinter.TOP, fill='x', padx=20, pady=(20, 0))
        self.topbar_container.pack_propagate(False)
        ###### Topbar ######

        ###### Main Container ######
        self.main_container = tkinter.Frame(self.root, bg="#D9D9D9")
        self.main_container.pack(fill='both', expand=True, padx=20, pady=20)
        ###### Main Container ######

        ###### Sidebar ######
        self.sidebar_container = tkinter.Frame(self.main_container, bg="#BDBDBD", width=200)
        self.sidebar_container.pack(side=tkinter.LEFT, fill='y')
        self.sidebar_container.pack_propagate(False)
        
        self.telas_container = tkinter.Frame(self.main_container, bg="#BDBDBD")
        self.telas_container.pack(side=tkinter.LEFT, fill='both', expand=True, padx=(20, 0))
        ###### Sidebar ######

        ###### Telas ######
        self.telas_container.grid_columnconfigure(0, weight=1)
        self.telas_container.grid_columnconfigure(2, weight=1)
        self.telas_container.grid_rowconfigure(0, weight=1)
        self.telas_container.grid_rowconfigure(2, weight=1)
        ###### Telas ######

        self.frames["informar_renda"] = self.renda_view.create_frame_tela_renda(self, self.telas_container)
        self.frames["informar_renda"].grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.frames["adicionar_despesa"] = self.despesa_view.create_frame_tela_despesa(self, self.telas_container)
        self.frames["adicionar_despesa"].grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
        
        self.frames["atualizar_renda"] = self.renda_view.create_frame_update_renda(self, self.telas_container)
        self.frames["atualizar_renda"].grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.frames["atualizar_despesas"] = self.despesa_view.create_frame_update_despesa(self, self.telas_container)
        self.frames["atualizar_despesas"].grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.frames["inicio"] = self.renda_view.create_frame_tela_principal(self, self.telas_container)
        self.frames["inicio"].grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

        self.topbar.create_topbar(self, self.topbar_container)
        self.sidebar.create_sidebar(self.sidebar_container, self.sidebar_commands())

    def sidebar_commands(self):
        return {
            "Início": lambda: self.controller.handle_navigation("inicio"),    
            "Informar renda": lambda: self.controller.handle_navigation("informar_renda"),
            "Adicionar despesa": lambda: self.controller.handle_navigation("adicionar_despesa"),
            "Atualizar despesas": lambda: self.controller.handle_navigation("atualizar_despesas"),
            "Atualizar renda": lambda: self.controller.handle_navigation("atualizar_renda")
        }

    def show_frame(self, frame_name):
        if frame_name in self.frames:
            self.frames[frame_name].tkraise()

    def main_loop(self):
        self.root.mainloop()