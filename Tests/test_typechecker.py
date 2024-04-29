import pytest

from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.Vardec import Vardec
from Parser.AddExp import AdditionExp
from Parser.MultExp import MultiplicationExp
from Parser.PrimaryExp import IntegerLiteral
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import FalseExp
from Parser.PrimaryExp import Variable
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker

def test_typeofIntLiteral():
    code = IntegerLiteral(5)
    envSpace = TypeEnvironment() # Create a new type environment
    typecheck = Typechecker(envSpace=envSpace)

    assert isinstance(typecheck.typeOf(code), IntType), "Int Literal Type Check Failed"

def test_typeOfBoolean():
    code = TrueExp()
    envSpace = TypeEnvironment()
    typecheck = Typechecker(envSpace=envSpace)

    assert isinstance(typecheck.typeOf(code), BooleanType), "True/False Type Check Failed"

def test_typeOfAdditionExp():
    code = AdditionExp(1, "+", 2)
    envSpace = TypeEnvironment()
    typecheck = Typechecker(envSpace=envSpace)

    assert isinstance(typecheck.typeOf(code), IntType), "Addition Type Check Failed"

def test_typeOfMultiplicationExp():
    code = MultiplicationExp(1, "*", 2)
    envSpace = TypeEnvironment()
    typecheck = Typechecker(envSpace=envSpace)

    assert isinstance(typecheck.typeOf(code), IntType), "Multiplication Type Check Failed"
