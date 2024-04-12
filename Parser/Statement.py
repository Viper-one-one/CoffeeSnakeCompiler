from abc import ABC
from Parser.Exp import Exp
from Parser.Vardec import Vardec

class Statement(ABC):
    raise NotImplementedError("Statement is an abstract class, it should not be instantiated")

class VariableDec(Statement):
    vardec: Vardec
    
    def __init__(self, vardec: Vardec) -> None:
        self.vardec = vardec
        
class Assignment(Statement):
    exp: Exp
    pass

class WhileLoop(Statement):
    exp: Exp
    pass

class Break(Statement):
    pass

class Return(Statement):
    # Return, possibly void
    exp: Exp

    def __init__(self, exp: Exp) -> None:
        self.exp = exp

class IfOptionalElse(Statement):
    # Need to handle case of optional else ?
    exp : Exp
    statement: Statement
    optionalStatement: Statement 

    def __init__(self, exp: Exp, statement: Statement, optionalStatement : None):
        self.exp = exp
        self.statement = statement


class Block(Statement):
    pass
