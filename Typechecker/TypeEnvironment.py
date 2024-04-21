from Parser.TypesAndNames import Type
from Parser.PrimaryExp import Variable

class TypeEnvironment:
    type: Type
    var: Variable

    # Note: TypeEnvironment was handled in class using Map. Could Use Dict here?
    def __init__(self, parentEnv): # Note: Blocks of code may need a pointer to their parent environments i.e. global scope
        self.envSpace = {}
        self.parentEnv = parentEnv
    
    # Note: Need a function to add a variable and it's type to the Type Environment. Might belong elsewhere
    def extend(self, type: Type, var: Variable):
        self.type = type
        self.variable = var
        self.envSpace.update(var, type)