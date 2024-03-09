from Tokenizer import Token

class LeftParenToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, LeftParenToken)
    
    def __str__(self):
        return "LeftParenToken"
    
    def __hash__(self):
        return 16