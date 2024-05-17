from Tokenizer.Token import Token

class SymbolPair:
    
    def __init__(self, asString, asToken):
        self.asString = asString
        self.asToken = asToken

    def __eq__(self, other):
        if(isinstance(other, SymbolPair)):
            return (self.asString.eq(other.asString) and self.asToken.eq(other.asToken))
        else:
            return False

    def __str__(self):
        return ("SymbolPair(" + self.asString + ", " + self.asToken.str() + ")")

    def __hash__(self):
        return hash(self.asString) + hash(self.asToken)


    # Bryan A





