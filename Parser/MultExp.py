from abc import ABC

from Parser.CallExp import CallExp


class MultExp(ABC):
    pass # I can't use anything with the error

class MultiplicationExp(MultExp):
    left: CallExp
    op: str
    right: CallExp
    
    def __init__(self, left: CallExp, op: str, right: CallExp) -> None:
        self.left = left
        self.op = op
        self.right = right

class DivisionExp(MultExp):
    left: CallExp
    op: str
    right: CallExp
    
    def __init__(self, left: CallExp, op: str, right: CallExp) -> None:
        self.left = left
        self.op = op
        self.right = right