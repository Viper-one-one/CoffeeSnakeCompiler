class MethodName:
    name: str
    
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other):
        if isinstance(self, MethodName):
            return self.name == other.name
        return False