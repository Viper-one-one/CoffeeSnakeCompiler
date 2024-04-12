from Parser.Type import Type

# Vardec may need a superclass
class Vardec:
    varType: Type
    varName: str
    
    def __init__(self, varType: Type, varName: str) -> None:
        self.varType = varType
        self.varName = varName