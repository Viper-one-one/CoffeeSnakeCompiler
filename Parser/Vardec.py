from Parser.TypesAndNames.Type import Type
from Parser.PrimaryExp import Variable

# Vardec may need a superclass
class Vardec:
    varType: Type
    var: Variable
    
    def __init__(self, varType: Type, var: Variable):
        self.varType = varType
        self.var = var

    def __eq__(self, other):
        if isinstance(other, Vardec):
            return self.varType == other.varType and self.var == other.var
        return False
    
    def __str__(self):
        return f"Vardec({self.varType}, {self.var})"
    
    def __repr__(self):
        return f"Vardec({repr(self.varType)}, {repr(self.var)})"