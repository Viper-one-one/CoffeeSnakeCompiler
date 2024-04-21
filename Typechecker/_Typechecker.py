from Parser.Program import Program
from Parser.TypesAndNames import Type
from Typechecker.TypeEnvironment import TypeEnvironment

class Typechecker:
    program: Program
    envSpace: TypeEnvironment
    
    # Constructor
    def __init__(self, program, envSpace):
        self.program = program
        self.envSpace = envSpace
    
    # Should be the first function called, then call other typeCheck functions as needed
    def typecheckProgram():
        pass

    def typecheckClassDef():
        pass
    
    def typecheckMethodDef():
        pass

    def typecheckStmt():
        pass

    def typeOf(): # Obtain the type of an exp?
        pass
    
    # Check if variable has been declared somewhere in scope/env
    def typeOfVariable(self, name):
        if self.name in self.envSpace:
            pass


    
    
