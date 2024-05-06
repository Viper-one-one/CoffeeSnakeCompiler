class ClassName:
    name: str
    
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other):
        if isinstance(other, ClassName):
            return self.name == other.name