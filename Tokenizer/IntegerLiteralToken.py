from Tokenizer.Token import Token

class IntegerLiteralToken(Token):
    
    def __init__(self, value):
        self.value = value
        
    def __eq__(self, other):
        if isinstance(other, IntegerLiteralToken):
            return self.value == other.value
        return False
        
    def __repr__(self):
        return f"IntegerLiteralToken({self.value})"
        
    def __str__(self):
        return f"IntegerLiteralToken({self.value})"
    
    def __hash__(self):
        return 13