from abc import ABC
from Parser.CommaVardec import CommaVardec
from Parser.CommaExp import CommaExp
from Parser.Statement import Statement

class Constructor(ABC):
    commaVardec: CommaVardec
    commaExp: CommaExp
    statement: Statement

    def __init__(self, commaVardec: CommaVardec, commaExp: CommaExp, statement: Statement):
        pass




