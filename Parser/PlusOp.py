from Op import Op

class PlusOp(Op):

    def __repr__(self):
        return "+"

    def __eq__(self, other):
        return isinstance(other, PlusOp)

    def __str__(self):
        return "PlusOp"

    def __hash__(self):
        pass # Needs Hash Number





