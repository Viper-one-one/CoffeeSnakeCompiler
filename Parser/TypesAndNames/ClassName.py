class ClassName:
    name: str
    
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other):
        if isinstance(other, ClassName):
            return self.name == other.name
    
    def __str__(self):
        return f"ClassName({self.name})"
    
    def __repr__(self):
        return f"ClassName({repr(self.name)})"