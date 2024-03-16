from Tokenizer.Token import Token

class PrintlnToken(Token):

    def __eq__(self, other):
        return isinstance(other, PrintlnToken)

    def __str__(self):
        return "PrintlnToken"

    def __hash__(self):
        return 21