from Stmt import Stmt


class WhileStmt(Stmt):

    def __init__(self, exp, stmt):
        self.exp = exp
        self.stmt = stmt

    def __eq__(self, other):
        if isinstance(other, WhileStmt):
            return self.exp == other.exp and self.stmt == other.stmt
        return False

    def __hash__(self):
        return hash(self.exp) + hash(self.stmt)

    def __str__(self):
        return ("WhileStmt(" +
                str(self.exp) +
                ", " + str(self.stmt) + ")")
