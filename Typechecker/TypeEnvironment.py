from Parser.TypesAndNames import Type
from Parser.PrimaryExp import Variable

class TypeEnvironment:
    type: Type
    var: Variable

    def __init__(self):
        self.envSpace = dict() # TypeEnvironment was handled in class using Map, could use dictionaries
        self.parentEnv = None # Might need pointer to a parent environment

    def extend(self, var: Variable, type: Type):
        self.envSpace[var] = type

    def addParentEnv(self, newEnv: 'TypeEnvironment'):
        self.parentEnv = newEnv