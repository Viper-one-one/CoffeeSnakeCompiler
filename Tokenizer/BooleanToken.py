from Tokenizer import Token


class BooleanToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, BooleanToken)
    
    def __str__():
        return "BooleanToken"
    
    def __hash__(self) -> int:
        return 2