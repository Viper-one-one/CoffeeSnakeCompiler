from abc import ABC


class ClassDef(ABC):
    def __init__(self, classname, extendsname, vardecs, constructor, methoddefs):
        self.classname = classname
        self.extendsname = extendsname
        self.vardecs = vardecs
        self.constructor = constructor
        self.methoddefs = methoddefs





