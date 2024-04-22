from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.BreakToken import BreakToken
from Tokenizer.ClassToken import ClassToken
from Tokenizer.CommaToken import CommaToken
from Tokenizer.DivisionToken import DivisionToken
from Tokenizer.DotToken import DotToken
from Tokenizer.ElseToken import ElseToken
from Tokenizer.ExtendsToken import ExtendsToken
from Tokenizer.FalseToken import FalseToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.IfToken import IfToken
from Tokenizer.InitToken import InitToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
from Tokenizer.IntToken import IntToken
from Tokenizer.LeftCurlyBraceToken import LeftCurlyBraceToken
from Tokenizer.LeftParenToken import LeftParenToken
from Tokenizer.MethodToken import MethodToken
from Tokenizer.MultiplicationToken import MultiplicationToken
from Tokenizer.NewToken import NewToken
from Tokenizer.PrintlnToken import PrintlnToken
from Tokenizer.ReturnToken import ReturnToken
from Tokenizer.RightCurlyBraceToken import RightCurlyBraceToken
from Tokenizer.RightParenToken import RightParenToken
from Tokenizer.SemiColonToken import SemiColonToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.StringLiteralToken import StringLiteralToken
from Tokenizer.SubtractionToken import SubtractionToken
from Tokenizer.SuperToken import SuperToken
from Tokenizer.ThisToken import ThisToken
from Tokenizer.TrueToken import TrueToken
from Tokenizer.VoidToken import VoidToken
from Tokenizer.WhileToken import WhileToken
from Tokenizer.SymbolPair import SymbolPair
from Tokenizer.VarToken import VarToken
from Parser.TypesAndNames.MethodName import MethodName
from Parser.TypesAndNames.ClassName import ClassName
from Parser.PrimaryExp import IntegerLiteral
from Parser.CommaVardec import CommaVardec
from Parser.Constructor import Constructor
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
from Parser.MethodDef import MethodDef
from Parser.PrimaryExp import Variable
from Tokenizer._Lexer import Tokenizer
from Parser.ClassDef import ClassDef
# from Parser.CommaExp import CommaExp
from Parser.CallExp import CallExp
from Parser.MultExp import MultExp
from Parser.Program import Program
from Tokenizer.Token import Token
from Parser.Vardec import Vardec
from Parser.AddExp import AddExp

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
            return self.tokens[self.position]  # Assuming tokens is a list of token instances
        else:
            raise Exception(f"Error getting next token: end of input reached at position {self.position}")
            
        
    # Match token function
    def match(self, expected_token: Token):
        current_token = self.get_next_token()
        if isinstance(expected_token, type):
            # Match the current token to expected token type
            if isinstance(current_token, expected_token):
                self.position += 1
                return current_token
            else:
                raise ValueError(f"Syntax error: expected {expected_token}, but found {type(current_token).__name__}")
        else:
            # Match the current token to expected token instance
            if current_token == expected_token:
                self.position += 1
                return current_token
            else:
                raise ValueError(f"Syntax error: expected {expected_token}, but found {current_token}")
        
    # Parsing functions for each production rule
    def type_parse(self):
        token = self.get_next_token()
        match token:
            case IntToken():
                self.position += 1
                return IntType
            case BooleanToken():
                self.position += 1
                return BooleanType
            case VoidToken():
                self.position += 1
                return VoidType
            case _:
                raise Exception(f"Error parsing type: {token} at position {self.position}")
                
        
    def comma_exp_parse(self):
        pass
        
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

    def vardec_parse(self):
        var_type = self.type_parse()
        var_name = self.match(IdentifierToken)
        end = self.match(SemiColonToken)

        return Vardec(var_type, Variable(var_name.name, var_type))
        
    def statement_parse(self):
        pass
        
    def comma_vardec_parse(self):
        pass
        
    def method_def_parse(self):
        pass
    
    def class_def_parse(self):
        self.match(ClassToken) 

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