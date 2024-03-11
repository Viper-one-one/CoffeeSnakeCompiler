#importing as a class
from Tokenizer.Token import Token

class ClassToken(Token):
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ClassToken)
    
    def __str__():
        return "ClassToken"
    
    def __hash__(self):
        return 4