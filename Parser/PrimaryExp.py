from abc import ABC
from Parser.TypesAndNames.Type import Type
from Parser.CommaExp import CommaExp
from Parser.TypesAndNames.ClassName import ClassName
from Parser.Exp import Exp

class PrimaryExp(ABC):
    raise NotImplementedError("PrimaryExp is an abstract class, it should not be instantiated")

class Variable(PrimaryExp):
    name: str
    varType: Type
    
    def __init__(self, name: str, varType: Type):
        self.name = name
        self.varType = varType

class IntegerLiteral(PrimaryExp):
    value: int
    
    def __init__(self, value: int):
        self.value = value

class ParenExp(PrimaryExp):
    inner: Exp
    
    def __int__(self, inner: Exp):
        self.inner = inner

class ThisExp(PrimaryExp):
    def __init__(self):
        pass

class TrueExp(PrimaryExp):
    def __init__(self):
        pass

class FalseExp(PrimaryExp):
    def __init__(self):
        pass

class PrintlnExp(PrimaryExp):
    expression:  Exp
    
    def __init__(self, expression: Exp):
        self.expression = expression

class NewObjectExp(PrimaryExp):
    classname: ClassName
    variables: CommaExp
    
    def __init__(self, classname: ClassName, variables: CommaExp):
        self.classname = classname
        self.variables = variables