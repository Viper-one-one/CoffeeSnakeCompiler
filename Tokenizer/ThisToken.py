from Tokenizer.Token import Token

class ThisToken(Token):

    def __eq__(self, other):
        return isinstance(other, ThisToken)

    def __str__(self):
        return "ThisToken"

    def __hash__(self):
        return 28