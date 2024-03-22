from Tokenizer.Lexer import Tokenizer
import os

def main():
    # take sampleProgram.coffeesnake and tokenize it
    try :
        file_path = os.path.join(os.path.dirname(__file__), "Tests\\sample_program.coffeesnake")
        tokens = Tokenizer.tokenize(file_path)
        print(f"Tokens: {tokens}")
    except FileNotFoundError:       # if file not found, print error message and return
        print("File not found")
    except Exception as e:          # if any other error occurs, print error message and return
        print("Lexer failed because of\nError: ", e)
    finally:
        print("File closed")
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()