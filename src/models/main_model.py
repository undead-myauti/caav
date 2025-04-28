from typing import List
class Model():
    def __init__(self):
        pass
    
    def generate_reference(self, references: List):
        return f'({references[2]}, {references[1]}. {references[0]})'
