from Tokenizer.Token import Token

class StringLiteralToken(Token):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, StringLiteralToken) and self.value == other.value

    def __str__(self):
        return f"StringLiteralToken({self.value})"

    def __hash__(self):
        return 27
