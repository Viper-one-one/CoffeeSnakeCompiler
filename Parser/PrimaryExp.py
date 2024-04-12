from abc import ABC
from Parser.CommaExp import CommaExp

from Parser.Exp import Exp

class PrimaryExp(ABC):
    pass

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
    classname: str
    variables: CommaExp
    
    def __init__(self, classname: str, variables: CommaExp):
        self.classname = classname
        self.variables = variables