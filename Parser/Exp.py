from abc import ABC


class Exp(ABC):
    pass

class IntegerLiteralExp(Exp(value)):
    def __init__(self, value):
        self.value = value

class TrueExp(Exp):
    pass

class FalseExp(Exp):
    pass

class BinOpExp(leftExp, op, rightExp):
    def __init__(self, leftExp, op, rightExp):
        self.leftExp = leftExp
        self.op = op
        self.rightExp = rightExp



