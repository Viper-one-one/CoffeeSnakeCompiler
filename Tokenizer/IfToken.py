import Token

class IfToken(Token):
    
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, IfToken)

    def __str__(self):
        return "IfToken"

    def __hash__(self):
        return 8




