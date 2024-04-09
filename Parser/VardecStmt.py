from Stmt import Stmt


class VardecStmt(Stmt):

    def __init__(self, type, variable, exp):
        self.type = type
        self.variable = variable
        self.exp = exp

    def __eq__(self, other):
        if isinstance(other, VardecStmt):
            return (self.exp == other.exp
                    and self.variable == other.variable
                    and self.type == other.type)
        return False

    def __hash__(self):
        return (hash(self.exp) +
                hash(self.variable) +
                hash(self.type))

    def __str__(self):
        return f"VardecStmt({str(self.type)}, {str(self.variable)}, {str(self.exp)})"
    