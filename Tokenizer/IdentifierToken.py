import string
#importing as a class
from Tokenizer.Token import Token

class IdentifierToken(Token):
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        if (isinstance(self, other)):
            return self.name == other.name
        return False
    
    def __str__(self):
        return f"IdentifierToken({self.name})"
        
    def __hash__(self):
        return 10