from Tokenizer.Token import Token

class SingleEqualsToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, SingleEqualsToken)

    def __str__(self):
        return "SingleEqualsToken"
    
    def __repr__(self):
        return "SingleEqualsToken"

    def __hash__(self):
        return 25