from Tokenizer._Lexer import Tokenizer


def main():
    tokenizer = Tokenizer("Tests//sample_program.txt")
    tokens = tokenizer.tokenize_file()
    print("Tokens", tokens)
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()