from abc import ABC

from Parser.Vardec import Vardec


class Statement(ABC):
    raise NotImplementedError("Statement is an abstract class, it should not be instantiated")

class VariableDec(Statement):
    vardec: Vardec
    
    def __init__(self, vardec: Vardec) -> None:
        self.vardec = vardec
        
class Assignment(Statement):
    

