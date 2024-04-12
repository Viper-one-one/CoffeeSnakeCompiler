from Parser.Type import Type

class Var(object):
    name: str
    varType: Type

    def __init__(self, name: str, varType: Type) -> None:
        self.name = name
        self.varType = varType