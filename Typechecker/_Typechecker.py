from Parser.Exp import Exp
from Parser.Exp import AddExp
from Parser.MultExp import MultExp
from Parser.Program import Program
from Parser.TypesAndNames import Type
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
from Parser.TypesAndNames.Type import classname
from Typechecker.TypeEnvironment import TypeEnvironment

class Typechecker:
    program: Program
    envSpace: TypeEnvironment
    
    # Constructor, initial env?
    def __init__(self, envSpace: TypeEnvironment):
        self.envSpace = envSpace

    # program ::= classdef* stmt+
    def typecheckProgram(self, program: Program):
        self.program = program
        # *Should begin type checking the classdefs/stmts in the program with initial empty env here*
        pass

    # methoddef ::= 'method' methodname '(' comma_vardec ')' type '{' stmt* '}'
    def typecheckMethod(self):
        pass

    # stmt ::= vardec ';' | var '=' exp ';' | 'while' '(' exp ')' stmt | ..... | exp ';'
    def typecheckStmt(self):
        pass

    # Obtain the type of an expression, i.e: 1 + 2. Return that type.
    def typeof(self, exp: Exp) -> Type:
        match exp:
            case AddExp():
                return IntType
            
            case MultExp():
                return IntType
            
            # case for bool type go here?

            # case for void type go here?

            

    
    
