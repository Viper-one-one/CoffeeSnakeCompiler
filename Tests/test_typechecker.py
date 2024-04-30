import pytest

from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.PrimaryExp import IntegerLiteral
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import Variable
from Parser.PrimaryExp import ParenExp
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker

# All tests must initialize a new Type Environment to pass to the Typechecker!
# Current number of tests: 4

def test_typeofIntLiteral():
    code = IntegerLiteral(5)
    envSpace = TypeEnvironment() 
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), IntType), "Int Literal Type Check Failed"

def test_typeofTrueExp():
    code = TrueExp()
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), BooleanType), "True/False Exp Type Check Failed"

def test_typeofVariable():
    code = Variable("my_int_variable", IntType())
    envSpace = TypeEnvironment()
    envSpace.extend(code.name, code.varType) # All variables must be added to the Type Environment!
    myTypechecker = Typechecker(envSpace=envSpace)
    
    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), IntType), "Variable w/ Int Type Check Failed"

def test_typeofParenExp():
    code = ParenExp(IntegerLiteral(5)) 
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace) 

    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), IntType), "Parenthesized Exp w/ Int Type Check Failed"

