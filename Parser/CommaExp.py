from Parser.Exp import Exp

class CommaExp(Exp):
    left: Exp
    right: Exp
    
    def __init__(self, left: Exp, right: Exp) -> None:
        self.left = left
        self.right = right