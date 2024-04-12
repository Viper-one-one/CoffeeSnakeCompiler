from Parser.CommaVardec import CommaVardec
from Parser.CommaExp import CommaExp
from Parser.Statement import Statement

class Constructor:
    commaVardec: CommaVardec
    commaExp: CommaExp
    statement: Statement

    def __init__(self, commaVardec: CommaVardec, commaExp: CommaExp, statement: Statement) -> None:
        self.commaVardec = commaVardec
        self.commaExp = commaExp
        self.statement = statement