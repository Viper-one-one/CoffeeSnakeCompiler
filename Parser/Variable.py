class Variable:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "Variable(" + str(self.name) + ")"
