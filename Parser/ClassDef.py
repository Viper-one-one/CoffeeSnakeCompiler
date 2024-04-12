from Parser.Vardec import Vardec
from Parser.Constructor import Constructor
from Parser.MethodDef import MethodDef
from Parser.ClassName import ClassName


class ClassDef:
    classname: ClassName
    extendsname: ClassName
    vardec: Vardec
    constructor: Constructor
    methodDef: MethodDef

    def __init__(self, classname: ClassName, extendsname: ClassName, vardecs: Vardec, constructor: Constructor, methoddefs: MethodDef):
        self.classname = classname
        self.extendsname = extendsname
        self.vardecs = vardecs
        self.constructor = constructor
        self.methoddefs = methoddefs





