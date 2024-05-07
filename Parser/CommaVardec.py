from typing import List
from Parser.Vardec import Vardec

class CommaVardec:
    vardecs: List[Vardec]

    def __init__(self, vardecs: List[Vardec]) -> None:
        self.vardecs = vardecs

    def __eq__(self, other):
        if isinstance(other, CommaVardec):
            return self.vardecs == other.vardecs
        return False

    def __str__(self):
        return f"CommaVardec({', '.join(map(str, self.vardecs))})"