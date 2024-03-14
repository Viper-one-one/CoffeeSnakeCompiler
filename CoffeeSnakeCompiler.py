from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.Token import Token

def main():
    token = AdditionToken()
    instance = isinstance(token, Token)
    print(instance)
    print("CoffeeSnake")
    
# this conditional runs the program when exe context is command line or as a file, it will NOT run under import module
if (__name__ == "__main__"):
    main()