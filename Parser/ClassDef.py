from Parser.Vardec import Vardec
from Parser.Constructor import Constructor
from Parser.MethodDef import MethodDef
from Parser.TypesAndNames.ClassName import ClassName
from typing import List


class ClassDef:
    classname: ClassName
    extendsname: ClassName
    vardec: List[Vardec]
    constructor: Constructor
    methodDef: List[MethodDef]

    def __init__(self, classname: ClassName, extendsname: ClassName, vardecs: List[Vardec], constructor: Constructor, methoddefs: List[MethodDef]):
        self.classname = classname
        self.extendsname = extendsname
        self.vardecs = vardecs
        self.constructor = constructor
        self.methoddefs = methoddefs

    def __eq__(self, other):
        if isinstance(other, ClassDef):
            return self.classname == other.classname and self.extendsname == other.extendsname and self.vardecs == other.vardecs and self.constructor == other.constructor and self.methoddefs == other.methoddefs
        return False
    
    def __str__(self):
        return f"ClassDef({self.classname}, {self.extendsname}, {self.vardecs}, {self.constructor}, {self.methoddefs})"
    
    def __repr__(self):
        return f"ClassDef({repr(self.classname)}, {repr(self.extendsname)}, {repr(self.vardecs)}, {repr(self.constructor)}, {repr(self.methoddefs)})"