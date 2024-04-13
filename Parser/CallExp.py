from Parser.CommaExp import CommaExp
from Parser.PrimaryExp import PrimaryExp
from Parser.TypesAndNames.MethodName import MethodName

# CallExp may need a superclass
class CallExp:
    left: PrimaryExp
    methodName: MethodName
    right: CommaExp

    def __init__(self, left: PrimaryExp, methodName: MethodName, right: CommaExp):
        self.left = left
        self.methodName = methodName
        self.right = right