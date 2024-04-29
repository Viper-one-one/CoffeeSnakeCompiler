from Parser.Exp import Exp
from Parser.AddExp import AdditionExp
from Parser.AddExp import SubtractionExp
from Parser.MultExp import MultiplicationExp
from Parser.MultExp import DivisionExp
from Parser.Program import Program
from Parser.PrimaryExp import PrimaryExp
from Parser.PrimaryExp import IntegerLiteral
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import FalseExp
from Parser.PrimaryExp import Variable
from Parser.TypesAndNames import Type
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
from Parser.TypesAndNames.Type import ClassName
from Typechecker.TypeEnvironment import TypeEnvironment

class Typechecker:
    program: Program
    envSpace: TypeEnvironment
    
    # Constructor 
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
            
    # Return the type of an expression. Our grammar does not support Strings. 
    # Nor do we support boolean operators, i.e.: <, >=, <=, &&, etc.
    # type ::= 'Int' | 'Boolean' | 'Void' | Classname 
    def typeOf(self, exp: Exp) -> Type:
        match exp:
            case AdditionExp():
                return IntType()
            
            case SubtractionExp():
                return IntType()
            
            case MultiplicationExp():
                return IntType()
            
            case DivisionExp():
                return IntType()
            
            case TrueExp() | FalseExp():
                return BooleanType()
            
            case PrimaryExp():
                match exp:
                    case IntegerLiteral():
                        return IntType()
                    
                    case Variable():
                        pass

                    
            

                    
                
                

 

            

    
    
