# probably needs work

class ParseResult:
    result: any
    next_position: int

    def __init__(self, result: any, next_position: int):
        self.result = result
        self.next_position = next_position