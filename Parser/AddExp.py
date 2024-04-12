from abc import ABC
from Parser.MultExp import MultExp


class AddExp(ABC):
    raise NotImplementedError("AddExp is an abstract class, it should not be instantiated")

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