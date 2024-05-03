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
from Parser.PrimaryExp import ParenExp
from Parser.PrimaryExp import ThisExp
from Parser.PrimaryExp import PrintlnExp
from Parser.PrimaryExp import NewObjectExp
from Parser.Vardec import Vardec
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

    def getProgramClassDefs(self):
        pass # Note: We will need a function to grab all classes defined in the program.
             #       as well as any parent classes, constructors and their parameters, and methods with their variables

    # non-recursive
    # add environment space for all the type checking methods
    # program ::= classdef* stmt+
    def typecheckProgram(self, program: Program, envSpace: TypeEnvironment):
        self.program = program
        # Note: Should begin type checking the classdefs/stmts in the program with initial empty env here
        pass

    #non-recursive
    # methoddef ::= 'method' methodname '(' comma_vardec ')' type '{' stmt* '}'
    def typecheckMethod(self):
        pass

    # recursive
    # stmt ::= vardec ';' | var '=' exp ';' | 'while' '(' exp ')' stmt | ..... | exp ';'
    def typecheckStmt(self, statement, currEnv):
        if isinstance(statement, Vardec):
            return Vardec()
        elif isinstance(statement, )

    # recursive
    # primary_exp ::= var | i | '(' exp ')' | 'this' | 'true' | 'false' | 'println' '(' exp ')' | 'new' classname '(' comma_exp ')'
    def typecheckExp(self, exp: Exp, currEnv: TypeEnvironment) -> Type: 
        if isinstance(exp, IntegerLiteral):
            return IntType()
        
        elif isinstance(exp, TrueExp):
            return BooleanType()
        
        elif isinstance(exp, FalseExp):
            return BooleanType()
        
        # *** Note: Don't forget to pass the current Environment ***
        elif isinstance(exp, Variable):
            return self.typeOfVariable(exp.name, currEnv) # Pass the variable's name to other function
        
        elif isinstance(exp, ParenExp):
            return self.typeOfPrimaryExp(exp.inner, currEnv) # Pass the inner exp recursively

        elif isinstance(exp, ThisExp):
            pass

        elif isinstance(exp, PrintlnExp):
            return self.typeOfPrimaryExp(exp.expression, currEnv) # Recursive call

        elif isinstance(exp, NewObjectExp):
            pass
            
    # non-recursive
    # looking for other Int x in scope and making sure that the assignment of x is to an Int    
    # Note: PrimaryExp has class Variable(name, varType)
    # Check if the variable exists in the current Environment. Return it's type. 
    def typecheckVariable(self, expressionName, currEnv: TypeEnvironment) -> Type:
        if expressionName in currEnv.envSpace:
            return currEnv.envSpace[expressionName] # Because we passed the current Env, we have access to the dictionary
        else:
            raise Exception(f"Error. No variable named {expressionName} found in your environmentSpace")

    def typecheckClass(self, className: ClassName, currEnv: TypeEnvironment):
        pass

    # Important Notes:
        # type ::= 'Int' | 'Boolean' | 'Void' | Classname 
        # Our grammar does not support Strings. 
        # Nor do we support boolean operators, i.e.: <, >=, <=, &&, etc.

                    
            

                    
                
                

 

            

    
    
