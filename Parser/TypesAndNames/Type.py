from abc import ABC

class Type(ABC):
    raise NotImplementedError("Type is an abstract class, it should not be instantiated")

class IntType(Type):   
    def __init__(self) -> None:
        pass

class BooleanType(Type):
    def __init__(self) -> None:
        pass

class VoidType(Type):
    def __init__(self) -> None:
        pass

class classname(Type):
    def __init__(self) -> None:
        pass