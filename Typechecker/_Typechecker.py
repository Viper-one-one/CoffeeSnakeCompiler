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
from Parser.TypesAndNames.ClassName import ClassName
from Parser.TypesAndNames.MethodName import MethodName
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
        elif isinstance(statement, None):
            pass

    # recursive
    # primary_exp ::= var | i | '(' exp ')' | 'this' | 'true' | 'false' | 'println' '(' exp ')' | 'new' classname '(' comma_exp ')'
    # exp --> add_exp --> mult_exp ---> call_exp --> primary_exp
    def typecheckExp(self, exp: Exp, currEnv: TypeEnvironment, definedClass: ClassName) -> Type: 
        # base level expressions
        if isinstance(exp, IntegerLiteral):
            return IntType()

        elif isinstance(exp, TrueExp):
            return BooleanType()
        
        elif isinstance(exp, FalseExp):
            return BooleanType()

        # *** Note: Don't forget to pass the current Environment ***
        elif isinstance(exp, Variable):
            return self.typecheckVariable(exp.name, currEnv) # Pass the variable's name to other function
        
        elif isinstance(exp, ParenExp):
            return self.typecheckExp(exp.inner, currEnv, definedClass) # Pass the inner exp recursively

        elif isinstance(exp, ThisExp):
            if definedClass is None:
                raise Exception("Incorrect use of 'this' without associated class")
            else:
                return ClassName(definedClass) # Return the associated class type

        elif isinstance(exp, PrintlnExp):
            return self.typecheckExp(exp.expression, currEnv, definedClass) # Recursive call

        elif isinstance(exp, NewObjectExp):
            pass
        
        elif isinstance(exp, ThisExp):
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
    

    # must check if the variables are initialized before they are used, checking if void is used as a value, checking that a function returning NOT void always returns
    
    # manage subtyping and method overloading

    # Important Notes:
        # type ::= 'Int' | 'Boolean' | 'Void' | Classname 
        # Our grammar does not support Strings. 
        # Nor do we support boolean operators, i.e.: <, >=, <=, &&, etc.

                    
            

                    
                
                

 

            

    
    
