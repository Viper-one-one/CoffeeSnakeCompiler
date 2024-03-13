from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.BreakToken import BreakToken
from Tokenizer.ClassToken import ClassToken
from Tokenizer.CommaToken import CommaToken
from Tokenizer.DivisionToken import DivisionToken
from Tokenizer.DotToken import DotToken
from Tokenizer.ElseToken import ElseToken
from Tokenizer.FalseToken import FalseToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.IfToken import IfToken
from Tokenizer.InitToken import InitToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
from Tokenizer.IntToken import IntToken
from Tokenizer.LeftCurlyBraceToken import LeftCurlyBraceToken
from Tokenizer.LeftParenToken import LeftParenToken
from Tokenizer.MethodToken import MethodToken
from Tokenizer.MultiplicationToken import MultiplicationToken
from Tokenizer.NewToken import NewToken
from Tokenizer.PrintlnToken import PrintlnToken
from Tokenizer.ReturnToken import ReturnToken
from Tokenizer.RightCurlyBraceToken import RightCurlyBraceToken
from Tokenizer.RightParenToken import RightParenToken
from Tokenizer.SemiColonToken import SemiColonToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.SubtractionToken import SubtractionToken
from Tokenizer.SuperToken import SuperToken
from Tokenizer.ThisToken import ThisToken
from Tokenizer.TrueToken import TrueToken
from Tokenizer.VoidToken import VoidToken
from Tokenizer.WhileToken import WhileToken
from Tokenizer.SymbolPair import SymbolPair

class Tokenizer(object):

    reserved_words = {
        "boolean": BooleanToken(),
        "break": BreakToken(),
        "class": ClassToken(),
        "else": ElseToken(),
        "false": FalseToken(),
        "init": InitToken(),
        "int": IntToken(),
        "if": IfToken(),
        "method": MethodToken(),
        "new": NewToken(),
        "println": PrintlnToken(),
        "return": ReturnToken(0),
        "super": SuperToken(),
        "this": ThisToken(),
        "true": TrueToken(),
        "void": VoidToken(),
        "while": WhileToken()
    }

    symbols = {
        "(": LeftParenToken(),
        ")": RightParenToken(),
        ".": DotToken(),
        "+": AdditionToken(),
        "-": SubtractionToken(),
        "*": MultiplicationToken(),
        "/": DivisionToken(),
        ",": CommaToken(),
        "{": LeftCurlyBraceToken(),
        "}": RightCurlyBraceToken(),
        ";": SemiColonToken(),
        "=": SingleEqualsToken()
    }

    def __init__(self, input_str: str):
        self.input = input_str
        self.position = 0
        
    def skip_whitespace(self):
        while self.position < len(input) and self.input[self.position].isspace():
            self.position += 1
            
    def readIntLiteralToken(self):
        digits: str = ""
        
        while self.position < len(self.input) and self.input[self.position].isdigit():
            digits += self.input[self.position]
            self.position += 1
        
        if digits:
            return IntegerLiteralToken(int(digits))
        else:
            return None

    def readSymbolToken(self):
        for symbol, token in symbols.items(): # Similar to for(final Pair<String, Token> pair : SYMBOLS) ?
            if self.input.startswith(symbol, position):
               position += len(symbol)
               return token
        return None

    def readReservedWordOrIdentifier(self):
        digits: str = ""
        if self.input.isalpha():
            digits += self.input[self.position]
            self.position += 1
            while self.position < len(self.input) and self.input[self.position].isalpha():
                digits += self.input[self.position]
                self.position += 1
            pass # TO DO: translate final Token Candidate = RESERVED_WORDS.get(characters) to python 


    def tokenizeSingle(self):
        if self.position < len(self.input): # Similar to assert(position < input.length) ?
            retVal = readIntegerLiteral()
            if retVal != None:
                return retVal

            retVal = readSymbolToken()
            if retVal != None:
                return retVal

            retVal = readReservedWordOrIdentifier()
            if retVal != None:
                return retVal
            else:
                pass # Should throw an exception here 


    def Tokenize(self):
        pass 

