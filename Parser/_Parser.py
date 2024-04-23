from Parser.TypesAndNames.MethodName import MethodName
from Parser.TypesAndNames.ClassName import ClassName
from Parser.PrimaryExp import IntegerLiteral
from Parser.CommaVardec import CommaVardec
from Parser.Constructor import Constructor
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
from Parser.TypesAndNames.Type import classname
from Parser.PrimaryExp import PrimaryExp
from Parser.MethodDef import MethodDef
from Parser.Statement import Statement
from Parser.PrimaryExp import Variable
from Tokenizer._Lexer import Tokenizer
from Parser.ClassDef import ClassDef
from Parser.CommaExp import CommaExp
from Parser.CallExp import CallExp
from Parser.MultExp import MultExp
from Parser.Program import Program
from Tokenizer.Token import Token
from Parser.Vardec import Vardec
from Parser.AddExp import AddExp
from Parser.Exp import Exp

class Parser:
    tokens: list
    position: int

    # Constructor
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.position = 0
        
    # Get next token function
    def get_next_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        else:
            raise Exception(f"Error getting next token: {self.position} and {self.position}")
        
    # Match token function
    def match_token(self, token: Token):
        rcv = self.get_next_token(self)
        if not rcv is token:
            raise Exception(f"Error matching token: {token} at position {self.position}")
        
    # Parsing functions for each production rule
    def type_parse(self):
        token = self.get_next_token()
        type_node = None
        match token:
            case IntType():
                type_node = IntType()
            case BooleanType():
                type_node = BooleanType()
            case VoidType():
                type_node = VoidType()
            case classname():
                type_node = classname()
            case _:
                raise Exception(f"Error parsing type: {token} at position {self.position}")
        self.position += 1
        return type_node        
        
    def comma_exp_parse(self):
        token = self.get_next_token()
        comma_exp_token = None
        match token:
            case 
        
    def primary_exp_parse(self):
        pass
        
    def call_exp_parse(self):
        pass
        
    def mult_exp_parse(self):
        pass

    def add_exp_parse(self):
        pass

    def exp_parse(self):
        pass

    def var_dec_parse(self):
        pass
        
    def statement_parse(self):
        pass
        
    def comma_vardec_parse(self):
        pass
        
    def method_def_parse(self):
        pass
    
    def class_def_parse(self):
        self.match_token(self, )
        self.match_token(self, )

    # outer production rule is the program entry point
    def program_parse(self):
        classDef = self.class_def_parse(self)
        statements = self.statement_parse(self)
        return Program(classDef, statements)

    # ATTENTION!
    # self contains the tokens list and the position
    # you can call self.get_next_token() to get the next token
    # you can call self.match_token(token) to match a token

    # program ::= classdef* stmt+ 

    # classdef ::= 'class' classname ['extends' classname] '{' (vardec ';')* constructor methodddef* '}'

    # constructor ::= 'init' '(' comma_vardec ')' '{' ['super' '(' comma_exp ')' ';'] stmt* '}'

    # stmt ::= vardec ';' | var '=' exp ';' | 'while' '(' exp ')' stmt | etc....

    # exp ::= add_exp

    # add_exp ::= mult_exp (( '+' | '-' ) mult_exp)*

    # mult_exp ::= call_exp (( '*' | '/' ) call_exp)*

    # call_exp ::= primary_exp('.' methodname '(' comma_exp ')' )*

    # primary_exp ::= var | str | i | etc....

    # comma_exp ::= exp (',' exp)*

    #                     AST Example: 2 + 2
    #                          Program
    #                             |
    #                             |
    #                         Statement
    #                             |
    #                             |
    #                       Binary Expression ( + )
    #                            /  \
    #                           /    \
    #                        (2)      (2)    