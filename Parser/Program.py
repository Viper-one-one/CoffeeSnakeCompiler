from abc import ABC
from Parser.ClassDef import ClassDef
from Parser.Statement import Statement 


class Program(ABC):
    classDef: ClassDef
    statement:  Statement 

    def __init__(self, classDef: ClassDef, statement: Statement):
       self.classDef = classDef
       self.statement = statement
       # Might need to have an array of statements?




