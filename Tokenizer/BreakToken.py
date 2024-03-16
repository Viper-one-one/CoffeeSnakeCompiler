from Tokenizer.Token import Token

class BreakToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, BreakToken)
    
    def __str__(self):
        return "BreakToken"
    
    def __repr__(self):
        return "BreakToken"  
    
    def __hash__(self):
        return 3