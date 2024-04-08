from Exp import Exp


class BinaryOpExp(Exp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, BinaryOpExp):
            return (self.op == other.op and
                    self.left == other.left and
                    self.right == other.right)
        return False

    def __hash__(self):
        return self.op.__hash__() + self.left.__hash__() + self.right.__hash__()

    def __str__(self):
        return ("BinaryOpExp(" + str(self.op) +
                ", " + str(self.left) + ", "
                + str(self.right) + ")")
