from Tokenizer._Lexer import Tokenizer
from Parser._Parser import Parser


def main():
    tokenizer = Tokenizer("var x = 7")
    tokens = tokenizer.tokenize()
    print("Tokens", tokens)
    parser = Parser(tokens)
    vardec = parser.parse_vardec()
    print(vardec)
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()