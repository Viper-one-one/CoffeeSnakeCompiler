from Parser import Type

class IntType(Type):

    def __eq__(self, other):
        return isinstance(other, IntType)

    def __str__(self):
        return "IntType"

    def __hash__(self):
        pass # Needs Hash Number




