from Parser.AddExp import AddExp

class Exp(AddExp):
    addExp: AddExp
    
    def __init__(self, addExp: AddExp) -> None:
        self.addExp = addExp