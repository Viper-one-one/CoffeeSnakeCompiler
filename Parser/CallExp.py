from Parser.CommaExp import CommaExp
from Parser.PrimaryExp import PrimaryExp

# should this be the super class of CallExp?
# what is the super class of CallExp?
class CallExp(PrimaryExp, CommaExp):
    left: PrimaryExp
    methodName: str
    right: CommaExp

    def __init__(self, left: PrimaryExp, methodName: str, right: CommaExp):
        self.left = left
        self.methodName = methodName
        self.right = right