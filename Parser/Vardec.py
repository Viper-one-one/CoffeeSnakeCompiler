from Parser.TypesAndNames.Type import Type
from Parser.PrimaryExp import Variable

# Vardec may need a superclass
class Vardec:
    varType: Type
    var: Variable
    
    def __init__(self, varType: Type, var: Variable):
        self.varType = varType
        self.var = var