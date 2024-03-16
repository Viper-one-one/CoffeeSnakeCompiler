from Tokenizer.Token import Token

class BooleanToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, BooleanToken)
    
    def __str__(self):
        return "BooleanToken"
    
    def __repr__(self):
        return "BooleanToken"  
      
    def __hash__(self) -> int:
        return 2