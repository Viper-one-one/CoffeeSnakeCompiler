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
from Tokenizer.ClassToken import ClassToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.ExtendsToken import ExtendsToken
from Tokenizer.LeftCurlyBraceToken import LeftCurlyBraceToken
from Tokenizer.RightCurlyBraceToken import RightCurlyBraceToken
from Tokenizer.IntToken import IntToken
from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.VarToken import VarToken
from Tokenizer.VoidToken import VoidToken


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens

    def get_next_token(self, position):
        if (0 <= position < len(self.tokens)):
            return self.tokens[position]
        else:
            raise Exception("Index out of bounds", position)

    def parse_program(self, pos):
        while True:
            node = self.parse_tokens()

    def parse_type(self, pos):
        pass

    def parse_comma_exp(self, pos):
        pass

    def parse_primary_exp(self, pos):
        pass

    def parse_call_exp(self, pos):
        pass

    def parse_mult_exp(self, pos):
        pass

    def parse_add_exp(self, pos):
        pass

    def parse_exp(self, pos):
        pass

    def parse_vardec(self, pos):
        token = self.tokens[pos]
        vartype = None
        if isinstance(token, IntToken):
            vartype = IntToken()
        elif isinstance(token, BooleanToken):
            vartype = BooleanToken()
        elif isinstance(token, VoidToken):
            vartype = VoidToken()
        elif isinstance(token, ClassToken):
            vartype = ClassToken()
        else:
            raise Exception("No type token found while parsing vardec")

        var, pos = self.parser_assert(pos, VarToken)
        vardec = Vardec(vartype, var)
        return vardec, pos + 1

    def parse_stmt(self, pos):
        pass

    def parse_comma_vardec(self, pos):
        pass

    def parse_methoddef(self, pos):
        pass

    def parse_constructor(self, pos):
        pass

    def parse_classdef(self, pos):
        pos = self.parser_assert(pos, ClassToken)

        classname = self.tokens[pos]
        extendsname = None

        try:
            extendsname, pos = self.parser_assert(pos, ExtendsToken)
        except:
            pass

        pos = self.parser_assert(pos, LeftCurlyBraceToken)

        vardecs = []
        try:
            while True:
                vardec, pos = self.parse_vardec(pos)
                vardecs.append(vardec)
        except:
            pass

        constructor, pos = self.parse_constructor(pos)

        methoddefs = []
        try:
            while True:
                methoddef, pos = self.parse_methoddef(pos)
                methoddefs.append(methoddef)
        except:
            pass

        pos = self.parser_assert(pos, RightCurlyBraceToken)

        classdef = ClassDef(classname, extendsname, vardecs, constructor, methoddefs)

        return classdef, pos + 1


    def parse_program(self, pos):
        pass

    def parser_assert(self, pos, type):
        token = self.tokens[pos]
        if not isinstance(token, type):
            raise Exception(f"Unexpected Token during Parsing: Expected {str(type)} received {str(token)}")

        return token, pos + 1
