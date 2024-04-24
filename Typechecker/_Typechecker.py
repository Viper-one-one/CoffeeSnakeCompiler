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
    
    # Constructor, initial environment space 
    def __init__(self, envSpace):
        self.envSpace = envSpace

    def typecheckProgram(self, program: Program):
        self.program = program
        pass

    # Obtain the type of an expression, i.e: (1 + 2). Our grammar does not support boolean operators.
    def typeof(self, exp: Exp) -> Type:
        match exp:
            case AddExp():
                return IntType
            
            case MultExp():
                return IntType
            
            # case for bool type

            # case for void type

            

    
    
