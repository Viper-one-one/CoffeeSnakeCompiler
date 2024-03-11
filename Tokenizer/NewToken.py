from Tokenizer import Token

class NewToken(Token):

    def __eq__(self, other):
        return isinstance(other, NewToken)

    def __str__(self):
        return "NewToken"

    def __hash__(self):
        return 19