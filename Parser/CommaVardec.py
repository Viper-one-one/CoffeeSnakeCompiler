from Parser.Vardec import Vardec

class CommaVardec:
    left: Vardec
    right: Vardec

    def __init__(self, left: Vardec, right: Vardec) -> None:
        self.left = left
        self.right = right