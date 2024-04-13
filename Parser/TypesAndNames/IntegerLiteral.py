# This file contains the IntegerLiteral class, which is used to represent integer literals in the AST.
# Differentiated from the Integer class, which is used to represent the integer type.
# i.e. IntegerLiteral(5): 5 and Integer(5): Int

class IntegerLiteral:
    value : int
    
    def __init__(self, value : int) -> None:
        self.value = value