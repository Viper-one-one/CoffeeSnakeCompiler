from Tokenizer._Lexer import Tokenizer
from Parser._Parser import Parser


def main():
    # tokenizer = Tokenizer("Tests//sample_program.txt")
    # tokens = tokenizer.tokenize_file()
    # print("Tokens", tokens)
    code = '2, true, this'
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    string_exp = parser.comma_exp_parse()  # Call the primary_exp_parse method to parse the code
    print(string_exp)

# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()