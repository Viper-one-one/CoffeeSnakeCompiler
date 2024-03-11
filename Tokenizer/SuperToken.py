#importing as a class
from Tokenizer.Token import Token

class SuperToken(Token):

    def __eq__(self, other):
        return isinstance(other, SuperToken)

    def __str__(self):
        return "SuperToken"

    def __hash__(self):
        return hash("SuperToken")