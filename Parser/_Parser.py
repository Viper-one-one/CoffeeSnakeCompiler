from Parser.AddExp import AddExp
from Parser.CallExp import CallExp
from Parser.ClassDef import ClassDef
from Parser.ClassName import ClassName
from Parser.CommaExp import CommaExp
from Parser.CommaVardec import CommaVardec
from Parser.Constructor import Constructor
from Parser.Exp import Exp
from Parser.IntegerLiteral import IntegerLiteral
from Parser.MethodDef import MethodDef
from Parser.MethodName import MethodName
from Parser.MultExp import MultExp
from Parser.PrimaryExp import PrimaryExp
from Parser.Program import Program
from Parser.Statement import Statement
from Parser.String import String
from Parser.Type import Type
from Parser.Var import Var
from Parser.Vardec import Vardec
from Tokenizer._Lexer import Tokenizer
from Tokenizer.Token import Token

class Parser:

    # Constructor
    def __init__(self, tokens):
        self.tokens = tokens
        self.input = ''

    def get_next_token(self, position):
        if (0 <= position < len(self.tokens)):
            return self.tokens[position]
        else:
            raise Exception("Index out of bounds", position)
        
    # type ::= Int | Boolean | Void | Class
    def parseType(self, position):
        typeToken = None
        for token in self.tokens: 
            if(token, isinstance(IntType)):
                 return IntType()
            elif(token, isinstance(BooleanType)):
                 return BooleanType()
                
            elif(token, isinstance(VoidType)):
                return VoidType
            
            elif(token, isinstance(ClassType)):
                return ClassType()
            else:
                raise Exception("Error Getting Type Token")

    # Parsing 
    def parse(self, input_str : str):
        self.input = input_str
        self.tokenizer = Tokenizer(input_str)
        tokens = self.tokenizer.tokenizeSingle(input_str)
        parse_program(tokens) # Start the AST pattern matching 
        
    # Potential Pattern Matching ?
    def parse_program(ast):
        match ast:
            case(ClassDef, *statements):
                return Program()
            
            case('class', ClassName, Vardec, Constructor, MethodDef):
                return ClassDef()
            
            case('class', ClassName, 'extends', *otherClassName, Vardec, Constructor, MethodDef):
                return ClassDef()
            
            case 'vardec' | 'var = exp;' | 'while (exp)' : # or break or return or if optional else or block 
                return Statement()
            
            case (Type, Var):
                return Vardec()
            
            case(CommaVardec, CommaExp, *statements):
                return Constructor()
            
            case(Vardec, *otherVarDecs):
                return CommaVardec()
            
            case('method', MethodName, CommaVardec, Type, *statements):
                return MethodDef()
            
            case(*AddExp): 
                return Exp()
            
            case(MultExp, *otherMultExps):
                return AddExp()
            
            case(CallExp, *otherCallExps):
                return MultExp()
            
            case(PrimaryExp, MethodName, CommaExp):
                return CallExp()
            
            case Var() | String() | IntegerLiteral(): # Or Paranthesized, Or This, Or True, Or PrintLn, or new Object
                return PrimaryExp()
            
            case(Exp, ',' , *otherExps):
                return CommaExp
            
            case _:
                return "Exception: Error Parsing"


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





