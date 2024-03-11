from Tokenizer import Token

class RightParenToken(Token):

    def __eq__(self, other):
        return isinstance(other, RightParenToken)

    def __str__(self):
        return "RightParenToken"

    def __hash__(self):
        return 23