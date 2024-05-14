from Parser.TypesAndNames import Type
from Parser.PrimaryExp import Variable

class TypeEnvironment:
    type: Type          # user made classes go in here
    var: Variable       # 
    envSpace: dict

    # needs to check if the variable is in the environment
    # if not, check the parent environment
    
    # add data structure to store the classes and their fields and methods
    # should hold the instance variables for the class and the parent class
    # no name shadowing, just reject
    # something like: methods = {
    # "method_name1": {"parameters": ["param1", "param2"], "return_type": "return_type"},
    # "method_name2": {"parameters": ["param1", "param2", "param3"], "return_type": "return_type"}
    # }
    
    # struct to store the method names, their parameters, and their return types
    
    # goal of a typechecker is to make sure that the stuff that could go wrong
    # in the program is caught

    def __init__(self):
        self.envSpace = dict() # dicts are maps in python
        self.parentEnv = None # Might need pointer to a parent environment

    def extend(self, var: Variable, type: Type):
        self.envSpace[var] = type
        
    def add(self, value, data):
        try :
            self.envSpace[value] = data
        except:
            raise Exception("Insertion failed.")

    def addParentEnv(self, newEnv: 'TypeEnvironment'):
        self.parentEnv = newEnv