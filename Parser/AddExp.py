from abc import ABC
from Parser.MultExp import MultExp

class AddExp(ABC):
    pass

class AdditionExp(AddExp):
    left: MultExp
    op: str
    right: MultExp
    
    def __init__(self, left: MultExp, op: str, right: MultExp) -> None:
        self.left = left
        self.op = op
        self.right = right

    def __eq__(self, other):
        if isinstance(self, AdditionExp):
            return self.left == other.left and self.op == other.op and self.right == self.right
        else:
            return False
    
    def __str__(self):
        return f"AdditionExp({self.left}, {self.op}, {self.right})"

class SubtractionExp(AddExp):
    left: MultExp
    op: str
    right: MultExp
    
    def __init__(self, left: MultExp, op: str, right: MultExp) -> None:
        self.left = left
        self.op = op
        self.right = right
    
    def __eq__(self, other):
        if isinstance(self, SubtractionExp):
            return self.left == other.left and self.op == other.op and self.right == self.right
        else:
            return False
    
    def __str__(self):
        return f"SubtractionExp({self.left}, {self.op}, {self.right})"
    