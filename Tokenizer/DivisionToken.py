import Token

class DivisionToken(Token):

    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, DivisionToken)

    def __str__(self):
        return "DivisionToken"

    def __hash__(self):
        return 4




