from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
from Tokenizer.Lexer import Tokenizer
from Tokenizer.IfToken import IfToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.VarToken import VarToken

def main():
    tokens = Tokenizer("var x = 7").tokenize()
    expected = [VarToken(), IdentifierToken("x"), SingleEqualsToken(), IntegerLiteralToken("7")]
    print(tokens)
    print(expected)
    print("CoffeeSnake")
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()