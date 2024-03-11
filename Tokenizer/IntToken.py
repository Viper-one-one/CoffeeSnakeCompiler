#importing as a class
from Tokenizer.Token import Token

class IntToken(Token):

    def __eq__(self, other):
        return isinstance(other, IntToken)

    def __str__(self):
        return "IntToken"

    def __hash__(self):
        return 34 

    # no code assigned in ListOfHashCodes.txt so used 34



