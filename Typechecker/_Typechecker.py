from Parser.Exp import Exp
from Parser.AddExp import AdditionExp
from Parser.AddExp import SubtractionExp
from Parser.MultExp import MultiplicationExp
from Parser.MultExp import DivisionExp
from Parser.Program import Program
from Parser.TypesAndNames import Type
from Parser.PrimaryExp import PrimaryExp
from Parser.PrimaryExp import IntegerLiteral
from Parser.PrimaryExp import StringLiteral
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import FalseExp
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
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


    # Note: Old typeOf Method
    #def typeof(self, exp: PrimaryExp):
     #   match exp:
      #      case IntegerLiteral():
       #         return IntType()
        #    
         #   case StringLiteral():
          #      return "StringType()"
            
    # Return the type of an expression. Note: Our grammar does not support boolean or string operators!
    def typeOf(self, exp: Exp):
        match exp:
            case AdditionExp():
                return IntType()
            
            case SubtractionExp():
                return IntType()
            
            case MultiplicationExp():
                return IntType()
            
            case DivisionExp():
                return IntType()
            
            case PrimaryExp():
                match exp:
                    case IntegerLiteral():
                        return IntType()
                    
                    case StringLiteral():
                        return "StringType()" # Note: Need String & Bool types?
                                              # type ::= 'Int' | 'Boolean' | 'Void' | classname
                
                

 

            

    
    
