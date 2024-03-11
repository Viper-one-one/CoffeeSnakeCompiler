from Tokenizer import Token

class DivisionToken(Token):

    def __eq__(self, other):
        return isinstance(other, DivisionToken)

    def __str__(self):
        return "DivisionToken"

    def __hash__(self):
        return 6