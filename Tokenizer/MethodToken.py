from Tokenizer.Token import Token

class MethodToken(object):
    
    def __eq__(self, other):
        return isinstance(other, MethodToken)

    def __str__(self):
        return "MethodToken"

    def __hash__(self):
        return 18