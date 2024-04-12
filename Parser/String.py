from Parser.Type import Type

class String:
    string: str
    varType: Type

    def __init__(self, string: str, varType: Type) -> None:
        self.string = string
        self.varType = varType




