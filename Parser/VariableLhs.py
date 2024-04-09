from Lhs import Lhs


class VariableLhs(Lhs):

    def __init__(self, variable):
        self.variable = variable

    def __eq__(self, other):
        return isinstance(other, VariableLhs) and self.variable == other.variable

    def __hash__(self):
        return hash(self.variable)

    def __str__(self):
        return "VariableLhs(" + str(self.variable) + ")"
