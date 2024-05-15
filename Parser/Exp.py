from Parser.AddExp import AddExp

class Exp:
    add_exp: AddExp

    def __init__(self, add_exp: AddExp) -> None:
        self.add_exp = add_exp
        
    def __eq__(self, __value) -> bool:
        if isinstance(AddExp, __value):
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f"Exp({self.add_exp})"
    
    def __hash__(self) -> int:
        return 23
