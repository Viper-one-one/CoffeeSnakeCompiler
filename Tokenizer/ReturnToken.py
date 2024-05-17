from Tokenizer.Token import Token

class ReturnToken(Token):

    def __eq__(self, other):
        return isinstance(other, ReturnToken)

    def __str__(self):
        return "ReturnToken"

    def __hash__(self):
        return 22