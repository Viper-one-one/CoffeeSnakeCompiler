from Tokenizer.Token import Token

class DotToken(Token):

    def __eq__(self, other):
        return isinstance(other, DotToken)

    def __str__(self):
        return "DotToken"

    def __hash__(self):
        return 7