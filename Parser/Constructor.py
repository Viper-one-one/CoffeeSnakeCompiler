from typing import List
from Parser.CommaVardec import CommaVardec
from Parser.CommaExp import CommaExp
from Parser.Statement import Statement

class Constructor:
    commaVardec: CommaVardec
    commaExp: CommaExp
    statement: List[Statement]

    def __init__(self, commaVardec: CommaVardec, commaExp: CommaExp, statement: List[Statement]) -> None:
        self.commaVardec = commaVardec
        self.commaExp = commaExp
        self.statement = statement

    def __eq__(self, other):
        if isinstance(other, Constructor):
            return self.commaVardec == other.commaVardec and self.commaExp == other.commaExp and self.statement == other.statement
        return False
    
    def __str__(self):
        return f"Constructor({self.commaVardec}, {self.commaExp}, {self.statement})"

    def __repr__(self):
        return f"Constructor({repr(self.commaVardec)}, {repr(self.commaExp)}, {repr(self.statement)})"