from Parser.AddExp import AddExp
from Parser.CallExp import CallExp
from Parser.ClassDef import ClassDef
from Parser.CommaExp import CommaExp
from Parser.CommaVardec import CommaVardec
from Parser.Constructor import Constructor
from Parser.Exp import Exp
from Parser.MethodDef import MethodDef
from Parser.MultExp import MultExp
from Parser.PrimaryExp import PrimaryExp
from Parser.Program import Program
from Parser.Statement import Statement
from Parser.Type import Type
from Parser.Vardec import Vardec
from Tokenizer._Lexer import Tokenizer

class Parser:

    # Constructor
    def __init__(self):
        self.input = ''
        self.Tokenizer = Tokenizer()

    # Parsing 
    def parse(self, input_str : str):
        self.input = input_str
        self.Toeknizer = Tokenizer.__init__(str)

        return Program() # Recursive Descent Parsing starts here

    # Root Node of AST
    parse_program = Program()  # Should return classdef and 1 or more statements






