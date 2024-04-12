from Parser.CommaExp import CommaExp
from Parser.PrimaryExp import PrimaryExp

# CallExp may need a superclass
class CallExp:
    left: PrimaryExp
    methodName: str
    right: CommaExp

    def __init__(self, left: PrimaryExp, methodName: str, right: CommaExp):
        self.left = left
        self.methodName = methodName
        self.right = right