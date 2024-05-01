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


    # program ::= classdef* stmt+
    def typecheckProgram(self, program: Program):
        self.program = program
        # Note: Should begin type checking the classdefs/stmts in the program with initial empty env here
        pass


    # methoddef ::= 'method' methodname '(' comma_vardec ')' type '{' stmt* '}'
    def typecheckMethod(self):
        pass


    # stmt ::= vardec ';' | var '=' exp ';' | 'while' '(' exp ')' stmt | ..... | exp ';'
    def typecheckStmt(self):
        pass


    # primary_exp ::= var | i | '(' exp ')' | 'this' | 'true' | 'false' | 'println' '(' exp ')' | 'new' classname '(' comma_exp ')'
    def typeOfPrimaryExp(self, exp: Exp, currEnv: TypeEnvironment) -> Type: 
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
            

    # Note: PrimaryExp has class Variable(name, varType)
    # Check if the variable exists in the current Environment. Return it's type. 
    def typeOfVariable(self, expressionName, currEnv: TypeEnvironment) -> Type:
        if expressionName in currEnv.envSpace:
            return currEnv.envSpace[expressionName] # Because we passed the current Env, we have access to the dictionary
        else:
            raise Exception(f"Error. No variable named {expressionName} found in your environmentSpace")
        

    # add_exp ::= mult_exp (('+' | '-') mult_exp)*
    def typeOfAddExp(self, exp, currEnv: TypeEnvironment) -> Type:
        if isinstance(exp, AdditionExp):
            left = exp.left
            op = exp.op
            right = exp.right
            
            if(isinstance(left, PrimaryExp) and isinstance(right, PrimaryExp)):
                typeOfLeft = self.typeOfPrimaryExp(left, currEnv)
                typeOfRight = self.typeOfPrimaryExp(right, currEnv)
                if(op == "+" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                    return IntType()
                else:
                    raise Exception(f"Invalid '+' operation with {exp.left} and {exp.right}")
                
            elif(isinstance(left, PrimaryExp) and isinstance(right, AdditionExp)):
                typeOfLeft = self.typeOfPrimaryExp(left, currEnv)
                typeOfRight = self.typeOfAddExp(right, currEnv)
                if(op == "+" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                     return IntType()
                else:
                     raise Exception(f"Invalid '+' operation with {exp.left} and {exp.right}")
            
            elif(isinstance(left, AdditionExp) and isinstance(right, PrimaryExp)):
                typeOfLeft = self.typeOfAddExp(left, currEnv)
                typeOfRight = self.typeOfPrimaryExp(right, currEnv)
                if(op == "+" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                    return IntType()
                else:
                    raise Exception(f"Invalid '+' operation with {exp.left} and {exp.right}")
    
        if isinstance(exp, SubtractionExp):
            left = exp.left
            op = exp.op
            right = exp.right

            if(isinstance(left, PrimaryExp) and isinstance(right, PrimaryExp)): 
                typeOfLeft = self.typeOfPrimaryExp(left, currEnv)
                typeOfRight = self.typeOfPrimaryExp(right, currEnv)
                if(op == "-" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                    return IntType()
                else:
                    raise Exception(f"Invalid '-' operation with {exp.left} and {exp.right}")
              # TODO Note: This case handles when input is SubtractionExp(AdditionExp(left, op, right), op, right).
              # We likely need to handle more cases, but this approach to handling AddExp might be inefficient, incorrect, or both 
            elif(isinstance(left, AdditionExp) and isinstance(right, PrimaryExp)):
                typeOfLeft = self.typeOfAddExp(left, currEnv)
                typeOfRight = self.typeOfPrimaryExp(right, currEnv)
                if(op == "-" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                    return IntType()
                else:
                    raise Exception(f"Invalid '-' operation with {exp.left} and {exp.right}")
                
            elif(isinstance(left, PrimaryExp) and isinstance(right, SubtractionExp)):
                typeOfLeft = self.typeOfPrimaryExp(left, currEnv)
                typeOfRight = self.typeOfAddExp(right, currEnv)
                if(op == "-" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                    return IntType()
                else:
                    raise Exception(f"Invalid '-' operation with {exp.left} and {exp.right}")


    # mult_exp ::= call_exp (('*' | '/') call_exp)*
    # TODO Note: May or may not have to do what was done in typeOfAddExp and do if statements for left and right class type
    def typeOfMultExp(self, exp, currEnv: TypeEnvironment):
        if isinstance(exp, MultiplicationExp):
            left = exp.left
            op = exp.op
            right = exp.right

            typeOfLeft = self.typeOfPrimaryExp(left, currEnv)
            typeOfRight = self.typeOfPrimaryExp(right, currEnv)

            if(op == "*" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                     return IntType()
            else:
                     raise Exception(f"Invalid '*' operation with {exp.left} and {exp.right}")
             
        if isinstance(exp, DivisionExp):
            left = exp.left
            op = exp.op
            right = exp.right

            typeOfLeft = self.typeOfPrimaryExp(left, currEnv)
            typeOfRight = self.typeOfPrimaryExp(right, currEnv)

            if(op =="/" and isinstance(typeOfLeft, IntType) and isinstance(typeOfRight, IntType)):
                return IntType()
            else:
                raise Exception(f"Invalid '/' operation with {exp.left} and {exp.right}")




    # Important Notes:
        # type ::= 'Int' | 'Boolean' | 'Void' | Classname 
        # Our grammar does not support Strings. 
        # Nor do we support boolean operators, i.e.: <, >=, <=, &&, etc.

                    
            

                    
                
                

 

            

    
    
