from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.IntToken import IntToken
from Tokenizer.IdentifierToken import IdentifierToken
from BoolType import BoolType
from IntType import IntType
class Parser():

    def __init__(self, tokens):
        self.tokens = tokens
    def parse_program(self):
        pass

    def getToken(self, position):
        if 0 <= position and position < len(self.tokens):
            return self.tokens[position]
        else:
            raise Exception("Invalid position:" + position)

    def assertTokenHereIs(self, position, expected):
        received = self.getToken(position)
        if expected != received:
            raise Exception("Expected: " + expected + "; received: " + received)

    def parseType(self, position):
        token = self.getToken(position)
        type = None
        if isinstance(token, IntToken):
            type = IntType()
        elif isinstance(token, BooleanToken):
            type = BoolType()
        elif isinstance(token, IdentifierToken):
            name = token.name
        else:
            raise Exception("Expected type; received: " + token)

        return type, position + 1
