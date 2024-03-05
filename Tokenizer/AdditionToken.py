import Token

class AdditionToken(Token):

    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, AdditionToken)

    def __str__(self):
        return "AdditionToken"

    def __hash__(self):
        return 2




