from abc import ABC
from Parser.CallExp import CallExp

class MultExp(ABC):
    pass

class MultiplicationExp(MultExp):
    left: CallExp
    op: str
    right: CallExp
    
    def __init__(self, left: CallExp, op: str, right: CallExp) -> None:
        self.left = left
        self.op = op
        self.right = right
    
    def __eq__(self, other):
        if isinstance(other, MultiplicationExp):
            return self.left == other.left and self.op == other.op and self.right == other.right
        return False
    
class DivisionExp(MultExp):
    left: CallExp
    op: str
    right: CallExp
    
    def __init__(self, left: CallExp, op: str, right: CallExp) -> None:
        self.left = left
        self.op = op
        self.right = right

    def __eq__(self, other):
        if isinstance(other, DivisionExp):
            return self.left == other.left and self.op == other.op and self.right == other.right
        return False