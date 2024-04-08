from Parser import Exp

class IntLiteralExp(Exp):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, IntLiteralExp):
            return self.value == other.value
        return False

    def __str__(self):
        return f"IntLiteralExp({self.value})"

    def __hash__(self):
        return self.value




