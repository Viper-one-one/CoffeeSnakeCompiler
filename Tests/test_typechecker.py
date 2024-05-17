import pytest

from Parser.Exp import Exp
from Parser.Vardec import Vardec
from Parser.TypesAndNames.Type import IntType, BooleanType
from Parser.TypesAndNames.ClassName import ClassName
from Parser.PrimaryExp import PrimaryExp, IntegerLiteral, TrueExp, FalseExp, Variable, ParenExp, PrintlnExp, ThisExp
from Parser.MultExp import MultiplicationExp, DivisionExp
from Parser.AddExp import AdditionExp, SubtractionExp
from Parser.CallExp import CallExp
from Parser.CommaExp import CommaExp
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker

# All tests must initialize a new Type Environment to pass to the Typechecker!
# Current number of tests: 11

def test_typeofIntLiteral():
    code = IntegerLiteral(5)
    code2 = TypeEnvironment()
    envSpace = TypeEnvironment() 
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code2, envSpace)

def test_typeofTrue_False_Exp():
    code = TrueExp()
    code2 = FalseExp()
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code2, envSpace), BooleanType)
    assert isinstance(myTypechecker.typecheckExp(code, envSpace), BooleanType)

def test_typeofVariable():
    code = Variable("my_int_variable", IntType())
    code2 = Variable("never_added_variable", BooleanType())
    envSpace = TypeEnvironment()
    envSpace.extend(code.name, code.varType) # All variables must be added to the Type Environment!
    myTypechecker = Typechecker(envSpace=envSpace)
    
    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)
    assert isinstance(myTypechecker.envSpace.lookUp(code.name, envSpace), IntType)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code2, envSpace)

def test_typeofParenExp():
    code = ParenExp(IntegerLiteral(5)) 
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace) 

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)

def test_typeofPrintLnExp():
    code = PrintlnExp(IntegerLiteral(10))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)


def test_typeofSubtractions():
    code_sub_and_add = SubtractionExp(AdditionExp(IntegerLiteral(5), "+", IntegerLiteral(10)), "-", IntegerLiteral(5))
    code_only_sub = SubtractionExp(IntegerLiteral(10), "-", IntegerLiteral(5))
    code3 = SubtractionExp(TrueExp(), "-", IntegerLiteral(5))
    code4 = SubtractionExp(IntegerLiteral(5), "-", FalseExp())
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_sub_and_add, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_sub, envSpace), IntType)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code3, envSpace)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code4, envSpace)

def test_typeofAdditions():
    code_only_add = AdditionExp(IntegerLiteral(7), "+", IntegerLiteral(5))
    code_add_and_sub = AdditionExp(IntegerLiteral(35), "+", SubtractionExp(IntegerLiteral(10), "-", IntegerLiteral(5)))
    code3 = AdditionExp(TrueExp(), "+", IntegerLiteral(5))
    code4 = AdditionExp(IntegerLiteral(10), "+", FalseExp())
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_add_and_sub, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_add, envSpace), IntType)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code3, envSpace)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code4, envSpace)


def test_typeofMultiplications():
    code_only_mult = MultiplicationExp(IntegerLiteral(5), "*", IntegerLiteral(3))
    code_add_and_mult= MultiplicationExp(AdditionExp(IntegerLiteral(5), "+", IntegerLiteral(5)), "*", IntegerLiteral(2))
    code3 = MultiplicationExp(TrueExp(), "*", IntegerLiteral(5))
    code4 = MultiplicationExp(IntegerLiteral(10), "*", FalseExp()) 
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_add_and_mult, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_mult, envSpace), IntType)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code3, envSpace)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code4, envSpace)

def test_typeofDivisions():
    code_only_div = DivisionExp(IntegerLiteral(20), "/", IntegerLiteral(5))
    code_two_adds_and_div = DivisionExp(AdditionExp(IntegerLiteral(50), "+", IntegerLiteral(50)), "/", AdditionExp(IntegerLiteral(1), "+", IntegerLiteral(1)))
    code3 = DivisionExp(TrueExp(), "/", IntegerLiteral(10))
    code4 = DivisionExp(IntegerLiteral(10), "/", FalseExp())
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_two_adds_and_div, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_div, envSpace), IntType)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code3, envSpace)
    with pytest.raises(Exception):
        myTypechecker.typecheckExp(code4, envSpace)

def test_typeofCommaExp():
    myVariable = Variable("num", IntType())
    code_addExp_trueExp_varExp = CommaExp([AdditionExp(IntegerLiteral(17), "+", IntegerLiteral(3)), TrueExp(), myVariable])
    code2 = CommaExp([TrueExp(), FalseExp()])
    envSpace = TypeEnvironment()
    envSpace.extend(myVariable.name, myVariable.varType)
    myTypechecker = Typechecker(envSpace=envSpace)

    assert myTypechecker.typecheckExp(code_addExp_trueExp_varExp, envSpace) == "Pass" 
    assert myTypechecker.typecheckExp(code2, envSpace) == "Pass"

def test_typeofCallExp(): #TODO this is a simple test case of CallExp
    code = CallExp(IntegerLiteral(10), None, None)
    code2 = CallExp(TrueExp(), None, None)
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code2, envSpace), BooleanType)

def test_parentEnvironments():
    # TOP
    # SECOND
    # THIRD
    code = Variable("Foo", IntType())
    code2 = Variable("Bar", BooleanType())

    topEnv = TypeEnvironment()
    topEnv.add(code.name, code.varType) # Top environment has variable "Foo"
    myTypechecker = Typechecker(topEnv)

    secondEnv = TypeEnvironment() # Second environment has nothing
    secondEnv.addParentEnv(topEnv)

    thirdEnv = TypeEnvironment()
    thirdEnv.extend(code2.name, code2.varType) # Third environment has access to variables "Foo" & "Bar"
    thirdEnv.addParentEnv(secondEnv)

    assert myTypechecker.envSpace.lookUp(code2.name, thirdEnv) == BooleanType()
    assert myTypechecker.envSpace.lookUp(code.name, thirdEnv) == IntType()
    with pytest.raises(Exception):
        myTypechecker.envSpace.lookUp(code2.name, topEnv)


    #assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)
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


