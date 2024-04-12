from abc import ABC
from Parser.ClassDef import ClassDef
from Parser.Statement import Statement 


class Program(ABC):
    classDef: ClassDef
    statements:  Statement 

    def __init__(self, classDef: ClassDef, statements: List[Statement]):
       self.classDef = classDef
       self.statements = statements





