class MethodName:
    name: str
    
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other):
        if isinstance(other, MethodName):
            return self.name == other.name
        return False
    
    def __str__(self):
        return f"MethodName({self.name})"
    
    def __repr__(self):
        return f"MethodName({repr(self.name)})"
    
    def __hash__(self) -> int:
        return hash(self.name)