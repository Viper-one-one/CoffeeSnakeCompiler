
class ClassName:
    
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, ClassName):
            return self.value == other.value
        return False

    def __str__(self):
        return f"ClassName({self.value})"

    def __hash__(self):
        pass # Needs hash number




