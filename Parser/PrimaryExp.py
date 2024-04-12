from abc import ABC


class PrimaryExp(ABC):
    pass

class varExp(Exp):
    def __init__(self, name):
        self.name = name

class integerExp(Exp):
    def __init__(self, num):
        self.num = num

class strExp(Exp):
    def __init__(self,string):
        self.string = string

class paranthesizedExp(Exp):
    def __init__(self, exp):
        self.exp = '(' + exp + ')'

class thisExp(Exp):
    pass
   
class trueExp(Exp):
    pass

class falseExp(Exp):
    pass

class printExp(Exp):
    pass

class newExp(Exp):
    pass



