from Exp import Exp


class BooleanLiteralExp(Exp):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, BooleanLiteralExp):
            return self.value == other.value
        return False

    def __str__(self):
        return f"BooleanLiteralExp({self.value})"

    def __hash__(self):
        if (self.value):
            return 1
        else:
            return 0
