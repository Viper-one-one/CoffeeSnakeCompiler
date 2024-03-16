from Tokenizer.Token import Token

class InitToken(Token):

    def __eq__(self, other):
        return isinstance(other, InitToken)

    def __str__(self):
        return "InitToken"
    
    def __repr__(self):
        return "InitToken"

    def __hash__(self):
        return 13




