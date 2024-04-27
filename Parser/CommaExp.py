from Parser.Exp import Exp
from typing import List

class CommaExp:
    expressions: List[Exp]
    
    def __init__(self, expressions: List[Exp]) -> None:
        self.expressions = expressions
