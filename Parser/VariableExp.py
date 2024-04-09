from Exp import Exp


class VariableExp(Exp):

    def __init__(self, variable):
        self.variable = variable

    def __eq__(self, other):
        return isinstance(other, VariableExp) and self.variable == other.variable

    def __hash__(self):
        return hash(self.variable)

    def __str__(self):
        return "VariableExp(" + str(self.variable) + ")"

