import Token

class SemiColonToken(Token):

    def __eq__(self, other):
        return isinstance(other, SemiColonToken)

    def __str__(self):
        return "SemiColonToken"

    def __hash__(self):
        return hash("SemiColonToken")