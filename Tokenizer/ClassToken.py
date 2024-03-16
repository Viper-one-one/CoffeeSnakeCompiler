from Tokenizer.Token import Token

class ClassToken(Token):

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ClassToken)
    
    def __str__(self):
        return "ClassToken"
    
    def __repr__(self):
        return "ClassToken"  
    
    def __hash__(self):
        return 4