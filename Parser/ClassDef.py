from abc import ABC
from Parser.Vardec import Vardec
from Parser.Constructor import Constructor
from Parser.MethodDef import MethodDef


class ClassDef(ABC):
    vardec: Vardec
    constructor: Constructor
    methodDef: MethodDef

    def __init__(self, classname, extendsname, vardecs, constructor, methoddefs):
        self.classname = classname
        self.extendsname = extendsname
        self.vardecs = vardecs
        self.constructor = constructor
        self.methoddefs = methoddefs





