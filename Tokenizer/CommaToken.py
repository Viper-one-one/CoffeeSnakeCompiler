from Tokenizer.Token import Token

class CommaToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, CommaToken)

    def __str__(self):
        return "CommaToken"

    def __hash__(self):
        return 5