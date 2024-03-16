from Tokenizer.Token import Token

class LeftCurlyBraceToken(Token):

    def __eq__(self, other):
        return isinstance(other, LeftCurlyBraceToken)

    def __str__(self):
        return "LeftCurlyBraceToken"
    
    def __repr__(self):
        return "LeftCurlyBraceToken"

    def __hash__(self):
        return 16