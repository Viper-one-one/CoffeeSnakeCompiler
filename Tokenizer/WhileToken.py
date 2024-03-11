#importing as a class
from Tokenizer.Token import Token

class WhileToken(Token):
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, WhileToken)

    def __str__(self):
        return "WhileToken"

    def __hash__(self):
        return hash("WhileToken")




