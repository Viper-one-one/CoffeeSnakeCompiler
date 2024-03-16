from Tokenizer.Token import Token

class ExtendsToken(Token):

    def __eq__(self, other):
        return isinstance(other, ExtendsToken)

    def __str__(self):
        return "ExtendsToken"
    
    def __repr__(self):
        return "ExtendsToken" 

    def __hash__(self):
        return 9