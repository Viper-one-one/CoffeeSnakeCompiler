from Parser import Op

class MultOp(Op):

    def __repr__(self):
        return "*"

    def __eq__(self, other):
        return isinstance(other, MultOp)

    def __str__(self):
        return "MultOp"

    def __hash__(self):
        pass # Needs Hash Number




