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

class Parser:
    
    reserved_words = {
        "class": ClassDef(),
        "Int": Type(),  # break these off into their subclasses later
        "Boolean": Type(),
        "Void": Type(),
        "if": Statement(),
        "while": Statement(),
        "return": Statement(),
        "break": Statement(),
        "this": PrimaryExp(),
        "new": PrimaryExp(),
        "true": PrimaryExp(),
        "false": PrimaryExp(),
        "println": PrimaryExp(),
        "super": Constructor(),
        
    }
    
    def __init__(self, tokens):
        self.tokens = tokens
    
    def get_next_token(self, position):
        if (0 <= position < len(self.tokens)):
            return self.tokens[position]
        else:
            raise Exception("Index out of bounds", position)
        
    def parse_program(self):
        while (True):
            if (self.get_next_token(0).value == "class"):
                self.parse_classdef()
            else:
                raise Exception("Expected class definition", self.get_next_token(0))
