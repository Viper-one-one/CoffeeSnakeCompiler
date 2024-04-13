from Parser.TypesAndNames.MethodName import MethodName
from Parser.TypesAndNames.ClassName import ClassName
from Parser.PrimaryExp import IntegerLiteral
from Parser.CommaVardec import CommaVardec
from Parser.Constructor import Constructor
from Parser.TypesAndNames.Type import Type
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

    # Constructor
    def __init__(self, tokens):
        self.tokens = tokens
        self.input = ''
        
    # Parsing functions for each production rule
    def type_parse():
        pass
        
    def comma_exp_parse():
        pass
        
    def primary_exp_parse():
        pass
        
    def call_exp_parse():
        pass
        
    def mult_exp_parse():
        pass

    def add_exp_parse():
        pass

    def exp_parse():
        pass

    def var_dec_parse():
        pass
        
    def statement_parse():
        pass
        
    def comma_vardec_parse():
        pass
        
    def method_def_parse():
        pass
    
    def class_def_parse():
        pass

    # outer production rule is the program entry point
    def program_parse():
        return Program()
            

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