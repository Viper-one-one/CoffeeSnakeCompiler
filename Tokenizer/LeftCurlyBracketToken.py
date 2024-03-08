from Tokenizer import Token

class LeftCurlyBracketToken(Token):

    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, LeftCurlyBracketToken)

    def __str__(self):
        return "LeftCurlyBracketToken"

    def __hash__(self):
        return 15



    # Bracket is 15, brace is 14

