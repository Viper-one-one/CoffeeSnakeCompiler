from Exp import Exp


class AccessExp(Exp):

    def __init__(self, exp, variable):
        self.exp = exp
        # professor is using optional class in java?
        self.expType = None
        self.variable = variable

    def __eq__(self, other):
        if isinstance(other, AccessExp):
            return (self.exp == other.exp and
                    self.expType == other.expType and
                    self.variable == other.variable)
        return False

    def __hash__(self):
        return hash(self.exp) + hash(self.expType) + hash(self.variable)

    def __str__(self):
        return ("AccessExp(" +
                str(self.exp) + ", " + str(self.expType) +
                ", " + str(self.variable) + ")")
