from Parser.CommaVardec import CommaVardec
from Parser.Statement import Statement
from Parser.Type import Type
from Parser.MethodName import MethodName


class MethodDef:
    methodname: MethodName
    parameters: CommaVardec
    return_type: Type
    body: Statement

    def __init__(self, methodname, parameters, return_type, body):
        self.methodname = methodname
        self.parameters = parameters
        self.return_type = return_type
        self.body = body