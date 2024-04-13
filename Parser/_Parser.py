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
from Tokenizer.VarToken import VarToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
import re

class Parser:

    # patterns = {
    #     r'\bvar\b': VarToken(),
    #     r'[a-zA-Z0-9_]*': IdentifierToken(),
    #     r'\b=\b': SingleEqualsToken(),
    #     r'\d+': IntegerLiteralToken(),
    # }

    # Constructor
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.current_index = -1

    # Parsing 
    def parse(self, input_str : str):
        self.input = input_str
        self.Tokenizer = Tokenizer(str)
        Program() # Prime the tokenizer to get the first token. Should classdef/return Statements?

    # classdef ::= `class` classname [`extends` classname] `{`
    #          (vardec `;`)*
    #          constructor
    #          methoddef*
    #          `}`

    def match_any(self, token_types):
        for token_type in token_types:
            token = self.match(token_type)
            if token:
                return token
        return None

    def parse_vardec(self):
        # token_patterns = {
        #     "VarToken": r'\bvar\b',
        #     "IdentifierToken": r'[a-zA-Z0-9_]+',
        #     "SingleEqualsToken": r'=',
        #     "IntegerLiteralToken": r'\d+'
        # }

        if (not type(self.tokens[0]) == VarToken or
            not type(self.tokens[1]) == IdentifierToken or
            not type(self.tokens[2]) == SingleEqualsToken or
            not type(self.tokens[3]) == IntegerLiteralToken):
                raise ValueError("Invalid syntax. Expected syntax: VarToken IdentifierToken SingleEqualsToken IntegerLiteralToken")

        # Initialize variables to store matched tokens
        var_name = None
        value = None

        # Iterate over tokens and match against corresponding patterns
        for token in self.tokens:
            if isinstance(token, VarToken):
                pass
            elif isinstance(token, IdentifierToken):
                var_name = token
            elif isinstance(token, SingleEqualsToken):
                pass  
            elif isinstance(token, IntegerLiteralToken):
                value = token.value

        # Check if all tokens are matched
        if all((var_name, value)):
            return Vardec(var_name, value)
        else:
            raise ValueError("Pattern does not match the input string.")


    # lazy val classDef: P[ClassDef] = {
    #     token(ClassToken) ~
    #     className ~
    #     opt(token(ExtendsToken) ~ className) ~
    #     inCurlyBrackets(rep(param ~ token(SemicolonToken)) ~ consDef ~ rep(methodDef)) ^^
    #     { case _ ~ name ~ opExtends ~ (params ~ consDef ~ methods) =>
    #       ClassDef(name, opExtends.map(_._2), params.map(_._1), consDef, methods) }
    #   }

    # program ::= classdef* stmt+ 

    # classdef ::= 'class' classname ['extends' classname] '{' (vardec ';')* constructor methoddef* '}'

    # vardec ::= type var


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





