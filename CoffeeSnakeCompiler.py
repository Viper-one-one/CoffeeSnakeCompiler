from Tokenizer._Lexer import Tokenizer
from Parser._Parser import Parser


def main():
    code = """
            class Animal {
            init() {}
            method speak() Void { return println(0); }
            }
           """
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    print("Tokens", tokens)
    parser = Parser(tokens)
    classdef = parser.parse_classdef()
    print(classdef)
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()