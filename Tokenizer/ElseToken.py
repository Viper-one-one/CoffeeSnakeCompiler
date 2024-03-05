import Token

class ElseToken(Token):

    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, ElseToken)

    def __str__(self):
        return "ElseToken"

    def __hash__(self):
        return 6




