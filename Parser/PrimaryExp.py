from abc import ABC


class PrimaryExp(ABC):
    pass

class VariableExp(Exp):
    pass

class StringExp(Exp):
    pass

class IntegerExp(Exp):
    pass

class ParanExp(Exp):
    pass

class ThisExp(Exp):
    pass

class TrueExp(Exp):
    pass

class FalseExp(Exp):
    pass

class PrintLnExp(Exp):
    pass

class NewExp(Exp):
    pass




