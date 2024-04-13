from abc import ABC
from Parser.MultExp import MultExp


class AddExp(ABC):
    pass # I can't use anything with the error

class AdditionExp(AddExp):
    left: MultExp
    op: str
    right: MultExp
    
    def __init__(self, left: MultExp, op: str, right: MultExp) -> None:
        self.left = left
        self.op = op
        self.right = right

class SubtractionExp(AddExp):
    left: MultExp
    op: str
    right: MultExp
    
    def __init__(self, left: MultExp, op: str, right: MultExp) -> None:
        self.left = left
        self.op = op
        self.right = right