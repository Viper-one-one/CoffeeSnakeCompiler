from Parser.TypesAndNames import Type
from Parser.PrimaryExp import Variable

class TypeEnvironment:
    type: Type
    var: Variable

    # Note: TypeEnvironment was handled in class using Map. Could Use Dict here?
    def __init__(self, parentEnv):
        self.envSpace = {}
        self.parentEnv = parentEnv
    
    # Need a function to add a variable and it's type to the Type Environment
    def extend(self, type: Type, var: Variable):
        self.type = type
        self.variable = var