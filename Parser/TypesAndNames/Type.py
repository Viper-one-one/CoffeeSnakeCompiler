from abc import ABC

class Type(ABC):
    raise NotImplementedError("Type is an abstract class, it should not be instantiated")

class IntType(Type):
    value: int
    
    def __init__(self, value: int) -> None:
        self.value = value

class BooleanType(Type):
    value: bool

    def __init__(self, value: bool) -> None:
        self.value = value

class VoidType(Type):
    def __init__(self) -> None:
        pass

class classname(Type):
    

    def __init__(self) -> None:
        pass
