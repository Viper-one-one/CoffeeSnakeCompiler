from Lhs import Lhs


class AccessLhs(Lhs):

    def __init__(self, lhs, variable):
        self.lhs = lhs
        self.lhsType = None
        self.variable = variable

    def __eq__(self, other):
        if isinstance(other, AccessLhs):
            return (self.lhs == other.lhs and
                    self.lhsType == other.lhsType and
                    self.variable == other.variable)
        return False

    def __hash__(self):
        return hash(self.lhs) + hash(self.lhsType) + hash(self.variable)

    def __str__(self):
        return ("AccessLhs(" + str(self.lhs) +
                ", " + str(self.lhsType) + ", "
                + str(self.variable) + ")")
