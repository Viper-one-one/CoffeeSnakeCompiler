from Parser.Exp import Exp
from typing import List

class CommaExp:
    expressions: List[Exp]
    
    def __init__(self, expressions: List[Exp]) -> None:
        self.expressions = expressions

    def __eq__(self, other):
        if not isinstance(other, CommaExp):
            return False
        return self.expressions == other.expressions

    def __str__(self):
        return f"CommaExp({self.expressions})"
    
    def __hash__(self) -> int:
        return 7
    