from Stmt import Stmt


class AssignStmt(Stmt):

    def __init__(self, lhs, exp):
        self.lhs = lhs
        self.exp = exp

    def __eq__(self, other):
        if isinstance(other, AssignStmt):
            return self.lhs == other.lhs and self.exp == other.exp
        return False

    def __hash__(self):
        return self.lhs.__hash__() + self.exp.__hash__()

    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + ", " + str(self.exp) + ")"
