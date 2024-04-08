from Parser import Exp

class ThisExp(Exp):

    def __eq__(self, other):
        return isinstance(other, ThisExp)

    def __str__(self):
        return "ThisExp"

    def __hash__(self):
        pass # Needs hash number




