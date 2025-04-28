import tkinter

class View:
    def __init__(self, controller):
        self.controller = controller

        self.root = tkinter.Tk()
        self.root.title("Gerador de Referências")

        self.firstContainer = tkinter.Frame(self.root)
        self.secondContainer = tkinter.Frame(self.root)
        self.thirdContainer = tkinter.Frame(self.root)

        self.firstContainer.pack()
        self.secondContainer.pack()
        self.thirdContainer.pack()

        self.container(self.firstContainer)
        self.container1(self.secondContainer)
        self.container2(self.thirdContainer)

    def container(self, container):
        self.labelNome = tkinter.Label(container, width=20, text="Nome:")
        self.labelSobrenome = tkinter.Label(container, width=20, text="Sobrenome:")
        self.labelAno = tkinter.Label(container, width=20, text="Ano:")

        self.entryNome = tkinter.Entry(container, width=20)
        self.entrySobrenome = tkinter.Entry(container, width=20)
        self.entryAno = tkinter.Entry(container, width=20)

        self.labelNome.pack()
        self.entryNome.pack()
        self.labelSobrenome.pack()
        self.entrySobrenome.pack()
        self.labelAno.pack()
        self.entryAno.pack()
    
    def container1(self, container):
        self.buttonRef = tkinter.Button(container, width=20, text="Gerar referência", command=self.call_update_reference)
        self.buttonLimpar = tkinter.Button(container, width=20, text="Limpar dados", command=self.clear_entries)

        self.buttonRef.pack()
        self.buttonLimpar.pack()

    def container2(self, container):
        self.labelRef = tkinter.Label(container, width=20, text="Referência:")
        self.labelInfo = tkinter.Label(container, width=40, text="xxxxxx")

        self.labelRef.pack()
        self.labelInfo.pack()

    def update_reference(self, reference: str):
        self.labelInfo['text'] = reference

    def call_update_reference(self):
        reference = self.controller.clickViewReference()
        self.update_reference(reference)

    def get_reference(self):
        return [
            self.entryAno.get(),
            self.entryNome.get(),
            self.entrySobrenome.get()
        ]

    def clear_entries(self):
        self.entryNome.delete(0, tkinter.END)
        self.entrySobrenome.delete(0, tkinter.END)
        self.entryAno.delete(0, tkinter.END)
        self.labelInfo['text'] = "xxxxxx"

    def main_loop(self):
        self.root.mainloop()