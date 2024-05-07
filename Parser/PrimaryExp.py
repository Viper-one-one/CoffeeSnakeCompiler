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
    
    def __init__(self, name: str, varType: Type = None): # set none since we're not checking types yet
        self.name = name
        self.varType = varType
    
    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.name == other.name and self.varType == self.varType
        return False

    def __str__(self):
        return f"Variable({self.name}, {self.varType})"
    
class IntegerLiteral(PrimaryExp):
    value: int
    
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, IntegerLiteral):
            return self.value == other.value
        return False

    def __str__(self):
        return f"IntegerLiteral({self.value})"
    
    def __repr__(self):
        return f"IntegerLiteral({repr(self.value)})"
    
class StringLiteral(PrimaryExp):
    value: str
    
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, StringLiteral):
            return self.value == other.value
        return False

    def __str__(self):
        return f"StringLiteral({self.value})"

class ParenExp(PrimaryExp):
    inner: Exp
    
    def __init__(self, inner: Exp):
        self.inner = inner

class ThisExp(PrimaryExp):
    def __init__(self):
        pass

    def __str__(self):
        return f"ThisExp()"

    def __eq__(self, other):
        return isinstance(other, ThisExp)

class TrueExp(PrimaryExp):
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, TrueExp)

    def __str__(self):
        return f"TrueExp()"
    

class FalseExp(PrimaryExp):
    def __init__(self):
        pass

class PrintlnExp(PrimaryExp):
    expression: Exp
    
    def __init__(self, expression: Exp):
        self.expression = expression

    def __eq__(self, other):
        if isinstance(other, PrintlnExp):
            return self.expression == other.expression
        return False
    
    def __str__(self):
        return f"PrintlnExp({self.expression})"
    
    def __repr__(self):
        return f"PrintlnExp({repr(self.expression)})"

class NewObjectExp(PrimaryExp):
    classname: ClassName
    variables: CommaExp
    
    def __init__(self, classname: ClassName, variables: CommaExp):
        self.classname = classname
        self.variables = variables

    def __eq__(self, other):
        if isinstance(other, NewObjectExp):
            return self.classname == other.classname and self.variables == other.variables
        return False

    def __str__(self):
        return f"NewObjectExp({self.classname}, {self.variables})"