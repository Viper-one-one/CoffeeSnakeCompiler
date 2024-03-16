from Tokenizer.Token import Token

class TrueToken(Token):
    def __eq__(self, other):
        return isinstance(other, TrueToken)

    def __str__(self):
        return "TrueToken"

    def __repr__(self):
        return "TrueToken"

    def __hash__(self):
        return 30