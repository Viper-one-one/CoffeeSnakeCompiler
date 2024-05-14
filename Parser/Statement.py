from abc import ABC
from Parser.Exp import Exp
from Parser.PrimaryExp import Variable
from Parser.Vardec import Vardec
from typing import List


class Statement(ABC):
    pass

class VariableDec(Statement):
    vardec: Vardec
    
    def __init__(self, vardec: Vardec) -> None:
        self.vardec = vardec
        
class Assignment(Statement):
    exp: Exp
    var: Variable
    
    def __init__(self, exp: Exp, var: Variable) -> None:
        self.exp = exp
        self.var = var
    
    def __eq__(self, other):
        if isinstance(other, Assignment):
            return self.exp == other.exp and self.var == other.var
        return False
    
    def __str__(self):
        return f"Assignment({self.exp}, {self.var})"
    
    def __repr__(self):
        return f"Assignment({repr(self.exp)}, {repr(self.var)})"
    
    def __hash__(self) -> int:
        return 16

class WhileLoop(Statement):
    exp: Exp
    stmt: Statement
    
    def __init__(self, exp: Exp, stmt: Statement) -> None:
        self.exp = exp
        self.stmt = stmt

    def __eq__(self, other):
        if isinstance(other, WhileLoop):
            return self.exp == other.exp and self.stmt == other.stmt
        return False

    def __str__(self):
        return f"WhileLoop({self.exp}, {self.stmt})"
    
    def __hash__(self) -> int:
        return 17

class Break(Statement):
    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        return isinstance(other, Break)
    
    def __hash__(self) -> int:
        return 18
    

class Return(Statement):
    exp: Exp

    def __init__(self, exp: Exp) -> None:
        self.exp = exp

    def __eq__(self, other):
        if isinstance(other, Return):
            return self.exp == other.exp
        return False
    
    def __str__(self):
        return f"Return({self.exp})"
    
    def __repr__(self):
        return f"Return({repr(self.exp)})"
    
    def __hash__(self) -> int:
        return 19

class IfOptionalElse(Statement):
    exp : Exp
    statement: Statement
    optionalStatement: Statement 

    def __init__(self, exp: Exp, statement: Statement, optionalStatement: Statement) -> None:
        self.exp = exp
        self.statement = statement
        self.optionalStatement = optionalStatement

    def __eq__(self, other):
        if isinstance(other, IfOptionalElse):
            return self.exp == other.exp and self.statement == other.statement and self.optionalStatement == other.optionalStatement
        return False
    
    def __str__(self):
        return f"IfOptionalElse({self.exp}, {self.statement}, {self.optionalStatement})"
    
    def __hash__(self) -> int:
        return 20

class Block(Statement):
    statements: List[Statement]

    def __init__(self, statements: List[Statement]) -> None:
        self.statements = statements

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.statements == other.statements
        return False
    
    def __str__(self):
        return f"Block({self.statements})"
    
    def __hash__(self) -> int:
        return 21
    