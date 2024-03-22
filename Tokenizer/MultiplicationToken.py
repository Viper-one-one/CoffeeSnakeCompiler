from Tokenizer.Token import Token

class MultiplicationToken(Token):

    def __eq__(self, other):
        return isinstance(other, MultiplicationToken)

    def __str__(self):
        return "MultiplicationToken"

    def __hash__(self):
        return 19