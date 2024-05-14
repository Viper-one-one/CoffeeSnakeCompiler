from abc import ABC

class Type(ABC):
    pass

class IntType(Type):   
    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        return isinstance(other, IntType)
    
    def __str__(self):
        return "IntType()"
    
    def __repr__(self):
        return "IntType()"

class BooleanType(Type):
    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        return isinstance(other, BooleanType)
    
    def __str__(self):
        return "BooleanType()"
    
    def __repr__(self):
        return "BooleanType()"

class VoidType(Type):
    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        return isinstance(other, VoidType)
    
    def __str__(self):
        return "VoidType()"
    
    def __repr__(self):
        return "VoidType()"
    
class ClassName(Type):
    def __init__(self) -> None:
        pass