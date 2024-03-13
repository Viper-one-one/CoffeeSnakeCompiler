from Tokenizer.Token import Token

class VoidToken(Token):
    def __eq__(self, other):
        return isinstance(other, VoidToken)

    def __str__(self):
        return "VoidToken"

    def __hash__(self):
        return 30