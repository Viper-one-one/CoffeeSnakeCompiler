from Parser.CommaExp import CommaExp
from Parser.AddExp import AdditionExp
from Parser.AddExp import SubtractionExp
from Parser.MethodDef import MethodDef
from Parser.MultExp import MultiplicationExp
from Parser.MultExp import DivisionExp
from Parser.Program import Program
from Parser.ClassDef import ClassDef
from Parser.Statement import Assignment, Block, Break, IfOptionalElse, Return, WhileLoop
from Parser.PrimaryExp import PrimaryExp, IntegerLiteral, TrueExp, FalseExp, Variable, ParenExp, ThisExp, PrintlnExp, NewObjectExp
from Parser.CallExp import CallExp
from Parser.Vardec import Vardec
from Parser.TypesAndNames import Type
from Parser.TypesAndNames.Type import IntType, BooleanType, VoidType
from Parser.TypesAndNames.ClassName import ClassName
from Parser.TypesAndNames.MethodName import MethodName
from Typechecker.TypeEnvironment import TypeEnvironment

class Typechecker:
    program: Program
    envSpace: TypeEnvironment
    

    # Constructor 
    def __init__(self, envSpace: TypeEnvironment):
        self.envSpace = envSpace

    def getProgramClassDefs(self, classdef_list: ClassDef, envSpace: TypeEnvironment):
        for classdef in classdef_list:
            envSpace.add(classdef.classname, classdef) # Note: Add the class name to the current environment space

    # non-recursive
    # add environment space for all the type checking methods
    # program ::= classdef* stmt+
    def typecheckProgram(self, program: Program, envSpace: TypeEnvironment):
        self.program = program
        # Note: Should begin type checking the classdefs/stmts in the program with initial empty env here
        self.getProgramClassDefs(program.classDef, envSpace) # add the class definitions to the environment space
        self.typecheckStmt(program.stmt, envSpace) # Note: This is where we begin type checking the statements in the program

    #non-recursive
    # methoddef ::= 'method' methodname '(' comma_vardec ')' type '{' stmt* '}'
    def typecheckMethod(self, method_def: MethodDef):
        self.envSpace.add(method_def.methodname, method_def.return_type, method_def.parameters)
        self.typecheckStmt(method_def.body, self.envSpace) # Note: Add the method name and type to the current environment)

    # recursive
    # stmt ::= vardec ';' | var '=' exp ';' | 'while' '(' exp ')' stmt | ..... | exp ';'
    def typecheckStmt(self, statement, currEnv):
        if isinstance(statement, Vardec):
            return self.typecheckVardec(statement, currEnv)
        elif isinstance(statement, Assignment):
            if statement.var in currEnv.envSpace:
                raise Exception(f"Error. Variable {statement.var} already exists in the current scope")
            else:
                currEnv.envSpace.add(statement.var, self.typecheckExp(statement.exp, currEnv))
                return # should return something?
        elif isinstance(statement, WhileLoop):
            if self.typecheckExp(statement.exp, currEnv) != BooleanType():
                raise Exception(f"Error. Expected boolean type in while loop condition")
            else:
                return self.typecheckStmt(statement.stmt, currEnv)
        elif isinstance(statement, Break):
            pass
        elif isinstance(statement, Return):
            if statement.exp is None:
                if currEnv.returnType != VoidType():
                    raise Exception(f"Error. Expected return type {currEnv.returnType}")
                else:
                    return
            elif statement.exp is not None:
                if self.typecheckExp(statement.exp, currEnv) != currEnv.returnType:
                    raise Exception(f"Error. Expected return type {currEnv.returnType}")
                else:
                    return
            else:
                raise Exception("Error. Return statement not recognized")
        elif isinstance(statement, IfOptionalElse):
            if self.typecheckExp(statement.exp, currEnv) != BooleanType():
                raise Exception(f"Error. Expected boolean type in if condition")
            elif statement.statement is not None:
                return self.typecheckStmt(statement.statement, currEnv)
            elif statement.optionalStatement is not None:
                return self.typecheckStmt(statement.optionalStatement, currEnv)
            else:
                raise Exception("Error. If statement not recognized")
        elif isinstance(statement, Block):
            return self.typecheckStmt(statement.stmt, currEnv)

    # make sure the vardec isn't trying to create a variable that already exists in the current environment
    # vardec ::= type var    
    # currEnv.add(vardec.var, vardec.varType)  
    def typecheckVardec(self, vardec: Vardec, currEnv: TypeEnvironment):
        if vardec.var.name in currEnv.envSpace: 
            raise Exception(f"{vardec.var.name} is already in the current Environment!")
        else: # Note: if the vardec's variable name doesn't already exist, then we add to the current environment?
            pass
    
    # recursive 
    # we recusrively call typecheckExp on the inner expressions as we move through the tree on ALL types of expressions, call, comma, primary, etc.
    # all exps ::= var | i | '(' exp ')' | 'this' | 'true' | 'false' | 'println' '(' exp ')' | 'new' classname '(' comma_exp ')' | [exp ( ',' exp)*] 
    # | primaryexp ('.' methodname '(' comma_exp ')')* | call_exp ((`*` | `/`) call_exp)* | mult_exp ((`+` | `-`) mult_exp)* | add_exp
    def typecheckExp(self, exp: Exp, currEnv: TypeEnvironment) -> Type: 
        # base level expressions
        if isinstance(exp, IntegerLiteral):
            return IntType()

        elif isinstance(exp, TrueExp):
            return BooleanType()
        
        elif isinstance(exp, FalseExp):
            return BooleanType()

        elif isinstance(exp, Variable):
            return self.typecheckVariable(exp.name, currEnv) 
        
        elif isinstance(exp, ParenExp):
            return self.typecheckExp(exp.inner, currEnv) 

        elif isinstance(exp, ThisExp):
            if exp in currEnv.envSpace:
                return currEnv.envSpace[exp]
            else:
                raise Exception(f"Error. {exp} not found in current environment space")

        elif isinstance(exp, PrintlnExp):
            return self.typecheckExp(exp.expression, currEnv) 

        elif isinstance(exp, NewObjectExp):
            if (exp.classname in currEnv.envSpace):
                return exp.classname        # still thinking about this one
        # Prof Notes: Make sure that the given class you're trying to make an instance of exists 
        # and that it has a constructor defined that takes the same # of parameters as those provided in new
        # and that the types of these parameters similarly line up with what's in the constructor
        
        elif isinstance(exp, CommaExp):
            listOfExpressions = exp.expressions # Grab list of exp 
            numberOfExpressions = 0 # Initialize a counter

            for exp in listOfExpressions:
                typeofCurrExp = self.typecheckExp(exp, currEnv)
                if isinstance(typeofCurrExp, IntType):
                    numberOfExpressions += 1
                    if numberOfExpressions == len(listOfExpressions): # Checked all expressions? You pass!
                        return "Pass" # Note: idk what to return
                elif isinstance(typeofCurrExp, BooleanType):
                    numberOfExpressions += 1
                    if numberOfExpressions == len(listOfExpressions):
                        return "Pass"

        elif isinstance(exp, CallExp):
            # Note: need to handle: ('.' methodname '(' comma_exp ')')*
            primaryExp = exp.left

            typeofprimaryExp = self.typecheckExp(primaryExp, currEnv)

            if isinstance(typeofprimaryExp, IntType):
                return IntType()
            elif isinstance(typeofprimaryExp, BooleanType):
                return BooleanType()
        
        elif isinstance(exp, MultiplicationExp):
            leftExp = exp.left
            rightExp = exp.right

            typeofLeft = self.typecheckExp(leftExp, currEnv)
            typeofRight = self.typecheckExp(rightExp, currEnv)

            # MULTIPLICATION
            if isinstance(typeofLeft, IntType) and isinstance(typeofRight, IntType):
                return IntType()
            elif not isinstance(typeofLeft, IntType):
                raise Exception(f"Error in Multiplication Exp. Left expression expected to be Int, recieved: {typeofLeft}")
            elif not isinstance(typeofRight, IntType):
                raise Exception(f"Error in Multiplication Exp. Right expression expected to be Int, recieved: {typeofRight}")
        
        elif isinstance(exp, DivisionExp):
            leftExp = exp.left
            rightExp = exp.right

            typeofLeft = self.typecheckExp(leftExp, currEnv)
            typeofRight = self.typecheckExp(rightExp, currEnv)

            # DIVISION
            if isinstance(typeofLeft, IntType) and isinstance(typeofRight, IntType):
                return IntType()
            elif not isinstance(typeofLeft, IntType):
                raise Exception(f"Error in Division Exp. Left expression expected to be Int, recieved {typeofLeft}")
            elif not isinstance(typeofRight, IntType):
                raise Exception(f"Error in Division Exp. Right expression expected to be Int, recieved: {typeofRight}")
        
        elif isinstance(exp, AdditionExp):
            leftExp = exp.left
            rightExp = exp.right

            typeofLeft = self.typecheckExp(leftExp, currEnv)
            typeofRight = self.typecheckExp(rightExp, currEnv)
            # ADDITION
            if isinstance(typeofLeft, IntType) and isinstance(typeofRight, IntType):
                return IntType()
            elif not isinstance(typeofLeft, IntType):
                raise Exception (f"Error in Addition Exp. Left expression expected to be Int, recieved: {typeofLeft}")
            elif not isinstance(typeofRight, IntType):
                raise Exception (f"Error in Addition Exp. Right expression expected to be Int, recieved: {typeofRight}")
        
        elif isinstance(exp, SubtractionExp):
            leftExp = exp.left
            rightExp = exp.right

            typeofLeft = self.typecheckExp(leftExp, currEnv)
            typeofRight = self.typecheckExp(rightExp, currEnv)
            # SUBTRACTION
            if isinstance(typeofLeft, IntType) and isinstance(typeofRight, IntType):
                return IntType()
            elif not isinstance(typeofLeft, IntType):
                raise Exception (f"Error in Subtraction Exp. Left expression expected to be Int, recieved: {typeofLeft}")
            elif not isinstance(typeofRight, IntType):
                raise Exception (f"Error in Subtraction Exp. Right expression expected to be Int, recieved: {typeofRight}")
            
        # End of the typecheckExp!
        else:
            raise Exception("Error. Expression not recognized.")
            
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
        if className in currEnv.envSpace:
            return currEnv.envSpace[className]
        else:
            raise Exception(f"Error. Class {className} not found in current environment space")
    

    # must check if the variables are initialized before they are used, checking if void is used as a value, checking that a function returning NOT void always returns
    
    # manage subtyping and method overloading

    # Important Notes:
        # type ::= 'Int' | 'Boolean' | 'Void' | Classname 
        # Our grammar does not support Strings. 
        # Nor do we support boolean operators, i.e.: <, >=, <=, &&, etc.
