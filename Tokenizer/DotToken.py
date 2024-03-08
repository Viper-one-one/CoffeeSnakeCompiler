from Tokenizer import Token

class DotToken(Token):
    
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, DotToken)

    def __str__(self):
        return "DotToken"

    def __hash__(self):
        return 7






