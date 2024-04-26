from abc import ABC
from typing import Union
from Parser.TypesAndNames.Type import Type
from Parser.CommaExp import CommaExp
from Parser.TypesAndNames.ClassName import ClassName

# Importing Exp here to resolve circular import
from Parser.Exp import Exp

class PrimaryExp(ABC):
    pass  # Simply have it do nothing if you don't want it instantiated

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

class StringLiteral(PrimaryExp):
    value: str
    
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, StringLiteral):
            return self.value == other.value
        return False

class ParenExp(PrimaryExp):
    inner: Exp
    
    def __init__(self, inner: Exp):
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
    expression: Exp
    
    def __init__(self, expression: Exp):
        self.expression = expression

class NewObjectExp(PrimaryExp):
    classname: ClassName
    variables: CommaExp
    
    def __init__(self, classname: ClassName, variables: CommaExp):
        self.classname = classname
        self.variables = variables
