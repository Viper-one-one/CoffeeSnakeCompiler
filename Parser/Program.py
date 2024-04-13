from Parser.ClassDef import ClassDef
from Parser.Statement import Statement 


class Program:
    classDef: ClassDef
    statements:  Statement 

    def __init__(self, classDef: ClassDef, statements: Statement) -> None:
       self.classDef = classDef
       self.statements = statements