from Parser.ClassDef import ClassDef
from Parser.Statement import Statement 
from typing import List

class Program:
    classDef: List[ClassDef]
    statements: List[Statement] 

    def __init__(self, classDef: List[ClassDef], statements: List[Statement]) -> None:
       self.classDef = classDef
       self.statements = statements

    def __eq__(self, other):
        if isinstance(other, Program):
            return self.classDef == other.classDef and self.statements == other.statements
        return False
    
    def __str__(self):
        return f"Program({self.classDef}, {self.statements})"
