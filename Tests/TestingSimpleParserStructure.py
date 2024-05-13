from Parser import Program, VariableDec, Vardec, AddExp, Assignment, PrimaryExp, Variable
from Parser.TypesAndNames import IntType

Program(VariableDec(Vardec(IntType, Variable)), VariableDec(Vardec(IntType, Variable)), VariableDec(Vardec(IntType, Variable)), Assignment(Variable, AddExp(Variable, Variable)))