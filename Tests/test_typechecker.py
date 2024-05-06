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

    assert isinstance(myTypechecker.typecheckExp(code, envSpace, None), IntType), "Int Literal Type Check Failed"

def test_typeofTrueExp():
    code = TrueExp()
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace, None), BooleanType), "True/False Exp Type Check Failed"

def test_typeofVariable():
    code = Variable("my_int_variable", IntType())
    envSpace = TypeEnvironment()
    envSpace.extend(code.name, code.varType) # All variables must be added to the Type Environment!
    myTypechecker = Typechecker(envSpace=envSpace)
    
    assert isinstance(myTypechecker.typecheckExp(code, envSpace, None), IntType), "Variable Exp w/ Int Type check failed!"

def test_typeofParenExp():
    code = ParenExp(IntegerLiteral(5)) 
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace) 

    assert isinstance(myTypechecker.typecheckExp(code, envSpace, None), IntType), "Parenthesized Exp w/ Int Type Check Failed"

def test_typeofPrintLnExp():
    code = PrintlnExp(IntegerLiteral(10))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace, None), IntType), "PrintLn Exp w/Int Type Check Failed"


def test_typeofThisExp():
    code = ThisExp()
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert ClassName("bar").__eq__(myTypechecker.typecheckExp(code, envSpace, "bar")), "ThisExp used without associated class!"


    #                     AST Example: Int x = 2 + 2
    #                          Program
    #                             |
    #                             |
    #                         Statement (var '=' exp)
    #                             |
    #                             |
    #                          add_exp
    #                            /  \
    #                           /    \
    #                    mult_exp     mult_exp
    #                        |            |
    #                        |            |
    #                    call_exp      call_exp
    #                        |            |
    #                        |            |
    #                  primary_exp   primary_exp
    #                        |            |
    #                        |            |
    #                       int          int


