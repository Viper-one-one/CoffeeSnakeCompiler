import Token

class RightCurlyBracketToken(Token):

    def __eq__(self, other):
        return isinstance(other, RightCurlyBracketToken)

    def __str__(self):
        return "RightCurlyBracketToken"

    def __hash__(self):
        return hash("RightCurlyBracketToken")