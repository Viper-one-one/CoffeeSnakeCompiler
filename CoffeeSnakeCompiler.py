import argparse
from Tokenizer._Lexer import Tokenizer
from Parser._Parser import Parser
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker


def main():
    code = argparse.ArgumentParser(description="Get the specified file")
    code.add_argument("file", type=str, help="The file to be compiled")
    
    args = code.parse_args()
    file_name = args.file
    
    # tokenizer = Tokenizer("Tests//sample_program.txt")
    # tokens = tokenizer.tokenize_file()
    # print("Tokens", tokens)
    tokenizer = Tokenizer(file_name)
    tokens = tokenizer.tokenize_file()
    print("Tokens", tokens)
    parser = Parser(tokens)
    string_exp = parser.program_parse()
    print("Parser AST", string_exp)
    envSpace = TypeEnvironment()
    type_checker = Typechecker(envSpace)
    type_checker.typecheckProgram(string_exp, envSpace)
    print(type_checker)

# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()