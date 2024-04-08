from Lhs import Lhs


class AccessThisLhs(Lhs):

    def __init__(self, variable):
        self.variable = variable
        self.targetType = None

    def __eq__(self, other):
        if isinstance(other, AccessThisLhs):
            return self.variable == other.variable and self.targetType == other.targetType
        return False

    def __hash__(self):
        return hash(self.variable) + hash(self.targetType)

    def __str__(self):
        return "AccessThisLhs(" + str(self.variable) + ", " + str(self.targetType) + ")"
