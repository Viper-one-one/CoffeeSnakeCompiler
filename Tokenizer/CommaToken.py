from Tokenizer import Token

class CommaToken(Token):
    
    def __init__(self):
        pass
    
    def __eq__(self, other):
        return isinstance(other, CommaToken)

    def __str__(self):
        return "CommaToken"

    def __hash__(self):
        return 5



