from typing import List
from Parser.CommaVardec import CommaVardec
from Parser.Statement import Statement
from Parser.TypesAndNames.Type import Type
from Parser.TypesAndNames.MethodName import MethodName

class MethodDef:
    methodname: MethodName
    parameters: CommaVardec
    return_type: Type
    body: List[Statement]

    def __init__(self, methodname, parameters, return_type, body):
        self.methodname = methodname
        self.parameters = parameters
        self.return_type = return_type
        self.body = body

    def __eq__(self, other):
        if isinstance(other, MethodDef):
            return self.methodname == other.methodname and self.parameters == other.parameters and self.return_type == other.return_type and self.body == other.body
        return False
    
    def __str__(self):
        return f"MethodDef({self.methodname}, {self.parameters}, {self.return_type}, {self.body})"
    
    def __repr__(self):
        return f"MethodDef({repr(self.methodname)}, {repr(self.parameters)}, {repr(self.return_type)}, {repr(self.body)})"
    
    def __hash__(self) -> int:
        return hash(self.methodname)
    