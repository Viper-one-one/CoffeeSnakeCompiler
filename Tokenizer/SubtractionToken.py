from Tokenizer.Token import Token

class SubtractionToken(Token):

    def __eq__(self, other):
        return isinstance(other, SubtractionToken)

    def __str__(self):
        return "SubtractionToken"

    def __repr__(self):
        return "SubtractionToken"

    def __hash__(self):
        return 26