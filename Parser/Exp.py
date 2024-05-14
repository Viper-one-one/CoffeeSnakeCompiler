from abc import ABC, abstractmethod

class Exp(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

class AddExp(Exp):
    def __init__(self, left: Exp, right: Exp) -> None:
        self.left = left
        self.right = right

    def evaluate(self) -> float:
        return self.left.evaluate() + self.right.evaluate()

class MultExp(Exp):
    def __init__(self, left: Exp, right: Exp) -> None:
        self.left = left
        self.right = right

    def evaluate(self) -> float:
        return self.left.evaluate() * self.right.evaluate()

class CallExp(Exp):
    def __init__(self, primary_exp: Exp, methodname: str, comma_exp: "CommaExp") -> None:
        self.primary_exp = primary_exp
        self.methodname = methodname
        self.comma_exp = comma_exp

    def evaluate(self) -> float:
        # Evaluate the result of the method call
        pass

# Define other expression types similarly
