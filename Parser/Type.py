from abc import ABC

class Type(ABC):
    pass # I can't use anything with the error

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
