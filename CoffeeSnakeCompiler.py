from Tokenizer._Lexer import Tokenizer
from Parser._Parser import Parser
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker


def main():
    # tokenizer = Tokenizer("Tests//sample_program.txt")
    # tokens = tokenizer.tokenize_file()
    # print("Tokens", tokens)
    code = """
                class Animal {
                init() {}
                method speak() Void { return println(0); }
                }
                class Cat extends Animal {
                init() { super(); }
                method speak() Void { return println(1); }
                }
                class Dog extends Animal {
                init() { super(); }
                method speak() Void { return println(2); }
                }
            """
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    string_exp = parser.program_parse()
    print(string_exp)
    envSpace = TypeEnvironment()
    type_checker = Typechecker(envSpace)
    type_checker.typecheckProgram(string_exp)

# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()