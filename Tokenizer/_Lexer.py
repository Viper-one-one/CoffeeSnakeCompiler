from io import TextIOWrapper
from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.BreakToken import BreakToken
from Tokenizer.ClassToken import ClassToken
from Tokenizer.CommaToken import CommaToken
from Tokenizer.DivisionToken import DivisionToken
from Tokenizer.DotToken import DotToken
from Tokenizer.ElseToken import ElseToken
from Tokenizer.ExtendsToken import ExtendsToken
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
from Tokenizer.VarToken import VarToken

# changed file name because Lexer was too burried in the file structure, _Lexer is now at the root of the Tokenizer folder

class Tokenizer(object):

    reserved_words = {
        "Boolean": BooleanToken(),      # Boolean, Int, and Void are all listed as uppercase in the grammar
        "break": BreakToken(),
        "class": ClassToken(),
        "else": ElseToken(),
        "extends": ExtendsToken(),
        "false": FalseToken(),
        "init": InitToken(),
        "Int": IntToken(),
        "if": IfToken(),
        "method": MethodToken(),
        "new": NewToken(),
        "println": PrintlnToken(),
        "return": ReturnToken(),
        "super": SuperToken(),
        "this": ThisToken(),
        "true": TrueToken(),
        "var": VarToken(),      # var token doesnt seem to be in the reserved words grammar, i.e. not in ''
        "Void": VoidToken(),
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
        self.lineNumber = 1
        self.charNumber = 1

    def skipWhitespace(self): #switched to camelCase for consistency
        while self.position < len(self.input) and self.input[self.position].isspace():
            if self.charNumber == 8 and self.lineNumber == 5:
                print("here")
            if self.input[self.position] in '\n':
                self.lineNumber += 1
                self.charNumber = 1
            self.position += 1
            self.charNumber += 1
            
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
        for symbol, token in self.symbols.items():
            if self.input.startswith(symbol, self.position):
               self.position += len(symbol)
               return token
        return None

    def readReservedWordOrIdentifier(self):
        if self.input[self.position].isalpha():
            read = []
            read.append(self.input[self.position])      # append the first character of the identifier to the list
            self.position += 1
            while (self.position < len(self.input) and (self.input[self.position].isdigit() or self.input[self.position].isalpha())):       # while the next character is alphanumeric
                read.append(self.input[self.position])      # valid identifiers are alphanumeric and reserved words are all letters
                self.position += 1
            asString = ''.join(read) # convert read into a string
            reservedWord = self.reserved_words.get(asString)
            if reservedWord != None:
                return reservedWord
            else: 
                return IdentifierToken(asString)
        else:
            return None

    def tokenizeSingle(self):
        self.skipWhitespace()
        if self.position < len(self.input):
            token = None
            # Attempt to tokenize the input in different ways
            if (token := self.readReservedWordOrIdentifier()) is None:
                if (token := self.readSymbolToken()) is None: # works
                    if (token := self.readIntLiteralToken()) is None: # works
                        # Unrecognized character
                        raise Exception(f"Unrecognized character: {token}\n\tAt line: {self.lineNumber}\n\tAt char {self.charNumber}")
            return token
        # error on println("), " is an unrecognized character and crashes lexer
        # is not in the grammar, need to clarify with prof about println("), variable declaration, and maybe more undiscovered cases
        else:
            return None

    def driver_tokenize(self):
        tokens = []
        token = None
        while True:
            token = self.tokenizeSingle()
            if (token != None):
                tokens.append(token)
            else:
                break
                print(f"Driver_Tokenizer failed on token: {token}")
        return tokens
    
    def object_creation_tokenize(input_str: str):
        return Tokenizer(input_str).driver_tokenize()
    
    def file_to_string_tokenize(file):
        try: 
            file_read_ouput = file.read()
            return Tokenizer.object_creation_tokenize(file_read_ouput)      # read() does not exist on string
        except FileNotFoundError as e:
            print(f"*\n*\n*\nLexer failed because of FileNotFound\nFile {e} not found\n*\n*\n*{file}")
            return None