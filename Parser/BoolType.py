from Type import Type

class BoolType(Type):

    def __eq__(self, other):
        return isinstance(other, BoolType)

    def __str__(self):
        return "BoolType"

    def __hash__(self):
        pass # Needs Hash Number




