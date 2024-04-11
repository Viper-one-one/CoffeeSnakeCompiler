from Tokenizer._Lexer import Tokenizer
import os

def main():
    try:
        folder_location = os.getcwd()
        sample_program_location = os.path.join(folder_location, "Tests\\sample_program.txt")
        with open(sample_program_location, 'r') as file_handle:
            tokens = Tokenizer.file_to_string_tokenize(file_handle)
        print(f"Tokens: {tokens}")
        parser = Tokenizer.parse(tokens)
        program = parser.parse_program()
        #type checker to be implemented below
    except Exception as e:          # general error catch, print error message and return
        print(f"*\n*\n*\nLexer failed because of generic failure\nError: {e}\n*\n*\n*")
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()