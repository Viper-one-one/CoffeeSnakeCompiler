from Tokenizer._Lexer import Tokenizer
import os

def main():
    # take sample_program.coffeesnake and tokenize it
    # file sample_program.coffeesnake not found error
    try:
        folder_location = os.getcwd()
        sample_program_location = os.path.join(folder_location, "Tests\\sample_program.txt")
        # test if file exists and is readable
        # sample = open(sample_program_location, 'r')
        # print(sample.read())
        # sample.close()
        with open(sample_program_location, 'r') as file_handle:
            tokens = Tokenizer.file_to_string_tokenize(file_handle)
        print(f"Tokens: {tokens}")
    except Exception as e:          # general error catch, print error message and return
        print(f"*\n*\n*\nLexer failed because of generic failure\nError: {e}\n*\n*\n*")
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()