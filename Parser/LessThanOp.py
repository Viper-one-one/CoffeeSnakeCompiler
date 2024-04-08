from Parser import Op

class LessThanOp(Op):

    def __repr__(self):
        return "<"

    def __eq__(self, other):
        return isinstance(other, LessThanOp)

    def __str__(self):
        return "LessThanOp"

    def __hash__(self):
        pass # Needs Hash Number




