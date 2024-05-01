from Parser.CommaExp import CommaExp
from Parser.PrimaryExp import PrimaryExp
from Parser.TypesAndNames.MethodName import MethodName
from abc import ABC

# CallExp may need a superclass
class CallingExp(ABC):
    pass

class CallExp(CallingExp):
    left: PrimaryExp
    methodName: MethodName
    right: CommaExp

    # call_exp ::= primary_exp ( '.' methodname '(' comma_exp ')' ) * 
    # methodname and commaexp are optional / zero or many
    def __init__(self, left: PrimaryExp, methodName: MethodName = None, right: CommaExp = None):
        self.left = left
        self.methodName = methodName
        self.right = right