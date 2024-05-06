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

    def __eq__(self, other):
        if isinstance(self, CallExp):
            return self.left == other.left and self.methodName == other.methodName and self.right == other.right
        return False
    
    def __str__(self):
        return f"CallExp({self.left}, {self.methodName}, {self.right})"