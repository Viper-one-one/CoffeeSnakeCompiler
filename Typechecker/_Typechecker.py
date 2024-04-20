from Parser.Program import Program
from Parser.TypesAndNames import Type

class Typechecker:
    program: Program
    
    # Constructor
    def __init__(self, program):
        self.program = program
    
    # Should be the first function called, then call other typeCheck functions as needed
    def typecheckProgram():
        pass

    def typecheckClassDef():
        pass
    
    def typecheckMethodDef():
        pass

    def typecheckStmt():
        pass

    
    # Check if variable has been declare somewhere in scope/env
    def typeOfVariable():
        pass


    
    
