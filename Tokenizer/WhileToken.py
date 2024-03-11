from Tokenizer import Token

class WhileToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, WhileToken)

    def __str__(self):
        return "WhileToken"

    def __hash__(self):
        return 31