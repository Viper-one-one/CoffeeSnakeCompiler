from Parser.Type import Type

class IntegerLiteral:
    value : int
    varType: Type
    
    def __init__(self, value : int, varType: Type) -> None:
        self.value = value
        self.varType = varType




