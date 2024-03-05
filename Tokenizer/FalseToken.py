import Token

class FalseToken(Token):
    
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, FalseToken)

    def __str__(self):
        return "FalseToken"

    def __hash__(self):
        return 7




