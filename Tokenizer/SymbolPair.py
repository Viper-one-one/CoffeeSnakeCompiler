from Tokenizer.Token import Token

class SymbolPair:
    
    def __init__(self, asString, asToken):
        self.asString = asString
        self.asToken = asToken

    def __eq__(self, other):
        if(isinstance(other, SymbolPair)):
            return (asString.eq(other.asString) and asToken.eq(other.asToken))
        else:
            return False

    def __str__(self):
        return ("SymbolPair(" + asString + ", " + asToken.str() + ")")
    
    def __repr__(self):
        return ("SymbolPair(" + asString + ", " + asToken.str() + ")")

    def __hash__(self):
        return hash(asString) + hash(asToken)


    # Bryan A





