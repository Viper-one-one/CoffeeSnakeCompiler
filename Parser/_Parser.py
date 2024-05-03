from Parser.AddExp import AddExp
from Parser.CallExp import CallExp
from Parser.ClassDef import ClassDef
from Parser.ClassName import ClassName
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
from Tokenizer.CommaToken import CommaToken
from Tokenizer._Lexer import Tokenizer
from Tokenizer.VarToken import VarToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
from Tokenizer.ClassToken import ClassToken
from Tokenizer.ExtendsToken import ExtendsToken
from Tokenizer.LeftCurlyBraceToken import LeftCurlyBraceToken
from Tokenizer.RightCurlyBraceToken import RightCurlyBraceToken
from Tokenizer.InitToken import InitToken
from Tokenizer.MethodToken import MethodToken

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
        self.current_index = 0

    # Parsing 
    def parse(self, input_str : str):
        self.input = input_str
        self.Tokenizer = Tokenizer(str)
        class_def = self.parse_class_def()
        statements = self.parse_statements()
        return Program(class_def, statements)
        # Prime the tokenizer to get the first token. Should classdef/return Statements?

    # classdef ::= `class` classname [`extends` classname] `{`
    #          (vardec `;`)*
    #          constructor
    #          methoddef*
    #          `}`

    # lazy val classDef: P[ClassDef] = {
    #     token(ClassToken) ~
    #     className ~
    #     opt(token(ExtendsToken) ~ className) ~
    #     inCurlyBrackets(rep(param ~ token(SemicolonToken)) ~ consDef ~ rep(methodDef)) ^^
    #     { case _ ~ name ~ opExtends ~ (params ~ consDef ~ methods) =>
    #       ClassDef(name, opExtends.map(_._2), params.map(_._1), consDef, methods) }
    #   }

    def match(self, expected_token_type):
        # Check if there are remaining tokens to parse
        if self.current_index < len(self.tokens):
            # Get the current token
            current_token = self.tokens[self.current_index]

            # Check if the current token matches the expected token type
            if isinstance(current_token, expected_token_type):
                # Move to the next token
                self.current_index += 1
                return current_token
            else:
                # If the current token doesn't match, raise a syntax error
                raise ValueError(f"Syntax error: expected {expected_token_type.__name__}, but found {type(current_token).__name__}")
        else:
            # If there are no more tokens to parse, return None
            return None

    def parse_classdef(self):
        # Check for the 'class' keyword
        self.match(ClassToken)

        # Parse the class name
        class_name_token = self.match(IdentifierToken)
        class_name = ClassName(class_name_token.name)

        # Initialize extended class name as None
        extended_class_name = None

        # Check if there is an 'extends' clause
        if self.tokens[self.current_index] == ExtendsToken:
            # Move past the 'extends' token
            self.current_index += 1

            # Parse the extended class name
            extended_class_name_token = self.match(IdentifierToken)
            extended_class_name = ClassName(extended_class_name_token.name)

        # Check for the '{' token
        self.match(LeftCurlyBraceToken)

        # Parse possible variable declarations
        vardecs = []
        while self.tokens[self.current_index] == VarToken:
            vardec = self.parse_vardec()
            vardecs.append(vardec)

        # Parse the contents of the class definition
        methods = []
        constructor = None

        while self.current_index < len(self.tokens) and self.tokens[self.current_index] != RightCurlyBraceToken:
            # Parse constructors
            if self.tokens[self.current_index] == InitToken:
                constructor = self.parse_constructor()

            # Parse methods
            elif self.tokens[self.current_index] == MethodToken:
                method = self.parse_method()
                methods.append(method)

            # Skip unknown tokens
            else:
                self.current_index += 1

        # Check for the '}' token
        self.match(RightCurlyBraceToken)

        token_strings = ' '.join(str(token) for token in self.tokens)
        print(token_strings)

        # Return the parsed class definition
        return ClassDef(class_name, extended_class_name, vardecs, constructor, methods)
    
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
    
    # token patterns: ExpToken
    def parse_comma_exp(self):
        self.match(Exp)
        left = self.parse_exp()
        if (self.tokens[self.current_index] == CommaToken):
            self.current_index += 1
            right = self.parse_exp()
            return CommaExp(left, right)
        else:
            self.current_index += 1
            return CommaExp(left, None)
        

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





