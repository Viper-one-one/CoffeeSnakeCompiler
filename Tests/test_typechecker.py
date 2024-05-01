import pytest

from Parser.Exp import Exp
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.ClassName import ClassName
from Parser.PrimaryExp import PrimaryExp
from Parser.PrimaryExp import IntegerLiteral
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import Variable
from Parser.PrimaryExp import ParenExp
from Parser.PrimaryExp import PrintlnExp
from Parser.PrimaryExp import ThisExp
from Parser.MultExp import MultiplicationExp
from Parser.AddExp import AdditionExp
from Parser.AddExp import SubtractionExp
from Parser.CallExp import CallExp
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker

# All tests must initialize a new Type Environment to pass to the Typechecker!
# Current number of tests: 7

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
    
    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), IntType), "Variable Exp w/ Int Type check failed!"

def test_typeofParenExp():
    code = ParenExp(IntegerLiteral(5)) 
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace) 

    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), IntType), "Parenthesized Exp w/ Int Type Check Failed"

def test_typeofPrintLnExp():
    code = PrintlnExp(IntegerLiteral(10))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typeOfPrimaryExp(code, envSpace), IntType), "PrintLn Exp w/Int Type Check Failed"

def test_typeofAddExp():
    additionCode = AdditionExp(IntegerLiteral(10), "+", IntegerLiteral(5))
    subtractionCode = SubtractionExp(IntegerLiteral(20), "-", IntegerLiteral(10))
    tripleAdditionCode = AdditionExp(IntegerLiteral(3), "+", AdditionExp(IntegerLiteral(6), "+", IntegerLiteral(9)))
    #tripleAdditionCode = SubtractionExp(AdditionExp(IntegerLiteral(5), "+", IntegerLiteral(10)), "-", IntegerLiteral(5))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typeOfAddExp(additionCode, envSpace), IntType), "Addition w/ Two Int Types Failed"
    assert isinstance(myTypechecker.typeOfAddExp(subtractionCode, envSpace), IntType), "Subtraction w/ Two Int Types Failed"
    assert isinstance(myTypechecker.typeOfAddExp(tripleAdditionCode, envSpace), IntType), "Triple addition failed"


def test_typeofMultExp():
    code = MultiplicationExp(IntegerLiteral(3), "*", IntegerLiteral(5))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)  
    assert isinstance(myTypechecker.typeOfMultExp(code, envSpace), IntType)

def test_typeofThisExp():
    pass # Note: Need to know the class we are in to determine the type of "this"


