from Tokenizer._Lexer import Tokenizer
import os

def main():
    # take sample_program.coffeesnake and tokenize it
    # file sample_program.coffeesnake not found error
    try:
        folder_location = os.getcwd()
        sample_program_location = os.path.join(folder_location, "Tests", "sample_program.txt")
        print(f"Sample program location: {sample_program_location}")
        # test if file exists and is readable
        # sample = open(sample_program_location, 'r')
        # print(sample.read())
        # sample.close()
        tokens = Tokenizer.tokenize(sample_program_location)
        print(f"Tokens: {tokens}")
    except Exception as e:          # general error catch, print error message and return
        print(f"*\n*\n*\nLexer failed because of\nError: {e}\n*\n*\n*")
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()