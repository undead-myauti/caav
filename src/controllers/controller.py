from src.models.main_model import Model
from src.views.main_view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(controller=self)

    def clickViewReference(self) -> str:
        references = self.view.get_reference()
        return self.model.generate_reference(references)

    def run(self):
        self.view.main_loop()