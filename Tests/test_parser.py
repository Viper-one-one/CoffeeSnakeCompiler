from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.ClassToken import ClassToken
from Parser.Parser import Parser

def test():
    b = BooleanToken()
    c = ClassToken()

    list = [b, c]

    p = Parser(list)

    p.assertTokenHereIs(1, c)