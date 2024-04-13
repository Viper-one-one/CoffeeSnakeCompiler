from Parser.Types.Type import Type

class Var:
    name: str
    varType: Type

    def __init__(self, name: str, varType: Type) -> None:
        self.name = name
        self.varType = varType