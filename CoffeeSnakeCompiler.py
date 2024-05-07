from Tokenizer._Lexer import Tokenizer
from Parser._Parser import Parser


def main():
    # tokenizer = Tokenizer("Tests//sample_program.txt")
    # tokens = tokenizer.tokenize_file()
    # print("Tokens", tokens)
    code = """class Cat extends Animal {
                    Int x; Boolean y; 
                    init() { super(); }
                    method speak() Void { return println(1); }
                    }
                    """
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    string_exp = parser.class_def_parse()
    print(string_exp)

# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()