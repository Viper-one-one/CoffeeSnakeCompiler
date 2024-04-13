from abc import ABC
from Parser.CommaExp import CommaExp
from Parser.ClassName import ClassName

from Parser.Exp import Exp

class PrimaryExp(ABC):
    pass # I can't use anything with the error

class Variable(PrimaryExp):
    name: str
    
    def __init__(self, name: str):
        self.name = name

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