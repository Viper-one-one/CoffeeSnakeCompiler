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
from Parser.PrimaryExp import StringLiteral
from Parser.PrimaryExp import ThisExp
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import FalseExp
from Parser.PrimaryExp import PrintlnExp
from Parser.PrimaryExp import NewObjectExp
from Tokenizer._Lexer import Tokenizer
from Parser.ClassDef import ClassDef
from Parser.CommaExp import CommaExp
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
        token = self.get_next_token()

        if isinstance(token, IdentifierToken):
            self.match(VarToken)
            return Variable(token.value)
        elif isinstance(token, StringLiteralToken):
            self.match(StringLiteralToken)  # Consume the token
            return StringLiteral(token.value)  # Return a StringLiteral object with the extracted value
        elif isinstance(token, IntegerLiteralToken):
            self.match(IntegerLiteralToken)  # Consume the token
            return IntegerLiteral(token.value) 
        elif isinstance(token, LeftParenToken):
            self.match(LeftParenToken)
            exp = self.exp_parse() 
            self.match(RightParenToken)
            return exp
        elif isinstance(token, ThisToken):
            self.match(ThisToken)
            return ThisExp()
        elif isinstance(token, TrueToken):
            self.match(TrueToken)
            return TrueExp()
        elif isinstance(token, FalseToken):
            self.match(FalseToken)
            return FalseExp()
        elif isinstance(token, PrintlnToken):
            self.match(PrintlnToken)
            return PrintlnExp()
        elif isinstance(token, NewToken):
            self.match(NewToken)
            return NewObjectExp() # needs more logic
        else:
            raise ValueError(f"Unexpected token: {token}")
        
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
        self.match(SemiColonToken)

        return Vardec(var_type, Variable(var_name.name, var_type))
    
    def assignment_parse(self):
        self.match(IdentifierToken)
        self.match(SingleEqualsToken)
        self.exp_parse()
        self.match(SemiColonToken)
        
    def statement_parse(self):
         # Check the type of statement and parse accordingly
        if self.get_next_token() in [IntToken, BooleanToken, VoidToken]:
            # Variable declaration statement
            return self.vardec_parse()
        elif self.get_next_token() == IdentifierToken:
            # Assignment statement
            return self.assignment_parse()
        elif self.get_next_token() == WhileToken:
            # While loop statement
            return self.while_parse()
        elif self.get_next_token() == BreakToken:
            # Break statement
            return self.break_parse()
        elif self.get_next_token() == ReturnToken:
            # Return statement
            return self.return_parse()
        elif self.get_next_token() == IfToken:
            # If statement
            return self.if_parse()
        elif self.get_next_token() == LeftCurlyBraceToken:
            # Block statement
            return self.block_parse()
        else:
            # If none of the above matches, raise an exception or handle accordingly
            raise ValueError(f"Unexpected token: {self.get_next_token()}")
        
    def comma_vardec_parse(self):
        var_decs = []

        var_dec = self.vardec_parse()
        var_decs.append(var_dec)

        # Check for additional variable declarations separated by commas
        while self.get_next_token() == CommaToken:
            self.match(CommaToken)  # Consume the comma token
            # Parse the next variable declaration
            var_dec = self.vardec_parse()
            var_decs.append(var_dec)

        return var_decs

        
    def method_def_parse(self):
        self.match(MethodToken)
        self.match(MethodName)
        self.match(LeftParenToken)
        self.comma_vardec_parse()
        self.match(RightParenToken)
        self.type_parse()
        self.match(LeftCurlyBraceToken)

    def constructor_parse(self):
        self.match(InitToken)
        self.match(LeftParenToken)

        #comma_vardec
        self.match(RightParenToken)
    

    #classdef ::= `class` classname [`extends` classname] `{`
    #  (vardec `;`)*
    #  constructor
    #  methoddef*
    #  `}`

    def class_def_parse(self):
        self.match(ClassToken)
        self.match(IdentifierToken)
        # needs an optional extends token
        if self.get_next_token() == ExtendsToken:
            self.match(ExtendsToken)
            superclass_name_token = self.match(IdentifierToken)
            # superclass_name = superclass_name_token.name # not sure why we're getting this..
        self.match(LeftCurlyBraceToken)

        while self.get_next_token() != RightCurlyBraceToken:
            # Parse variable declarations if encountered
            if self.get_next_token() in [IntToken, BooleanToken, VoidToken]:
                self.vardec_parse()
                self.match(SemiColonToken)
        # constructor

        self.match(RightCurlyBraceToken)

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

    #                     AST Example: Int x = 2 + 2
    #                          Program
    #                             |
    #                             |
    #                         Statement (var '=' exp)
    #                             |
    #                             |
    #                          add_exp
    #                            /  \
    #                           /    \
    #                    mult_exp     mult_exp
    #                        |            |
    #                        |            |
    #                    call_exp      call_exp
    #                        |            |
    #                        |            |
    #                  primary_exp   primary_exp
    #                        |            |
    #                        |            |
    #                       int          int