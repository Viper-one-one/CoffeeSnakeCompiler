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
    
    def __hash__(self) -> int:
        return 24

class BooleanType(Type):
    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        return isinstance(other, BooleanType)
    
    def __str__(self):
        return "BooleanType()"
    
    def __repr__(self):
        return "BooleanType()"
    
    def __hash__(self) -> int:
        return 25

class VoidType(Type):
    def __init__(self) -> None:
        pass

    def __eq__(self, other):
        return isinstance(other, VoidType)
    
    def __str__(self):
        return "VoidType()"
    
    def __repr__(self):
        return "VoidType()"
    
    def __hash__(self) -> int:
        return 26
    
class ClassName(Type):
    def __init__(self) -> None:
        pass
    
    def __eq__(self, other):
        return isinstance(other, ClassName)
    
    def __str__(self):
        return "ClassName()"
    
    def __repr__(self):
        return "ClassName()"
    
    def __hash__(self) -> int:
        return 27
    