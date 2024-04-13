from abc import ABC
from Parser.Exp import Exp
from Parser.Var import Var
from Parser.Vardec import Vardec

class Statement(ABC):
    pass # I can't use anything with the error

class VariableDec(Statement):
    vardec: Vardec
    
    def __init__(self, vardec: Vardec) -> None:
        self.vardec = vardec
        
class Assignment(Statement):
    exp: Exp
    var: Var
    
    def __init__(self, exp: Exp, var: Var) -> None:
        self.exp = exp
        self.var = var

class WhileLoop(Statement):
    exp: Exp
    stmt: Statement
    
    def __init__(self, exp: Exp, stmt: Statement) -> None:
        self.exp = exp
        self.stmt = stmt

class Break(Statement):
    def __init__(self) -> None:
        pass

class Return(Statement):
    exp: Exp

    def __init__(self, exp: Exp) -> None:
        self.exp = exp

class IfOptionalElse(Statement):
    exp : Exp
    statement: Statement
    optionalStatement: Statement 

    def __init__(self, exp: Exp, statement: Statement, optionalStatement: Statement) -> None:
        self.exp = exp
        self.statement = statement
        self.optionalStatement = optionalStatement


class Block(Statement):
    stmt: Statement
    
    def __init__(self, stmt: Statement) -> None:
        self.stmt = stmt
