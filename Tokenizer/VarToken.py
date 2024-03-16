#importing as a class
from Tokenizer.Token import Token

class VarToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, VarToken)
    
    def __str__(self):
        return "VarToken"
    
    def __repr__(self):
        return "VarToken"
    
    def __hash__(self):
        return 31