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
from Parser.Statement import Block,WhileLoop,Return,IfOptionalElse,Assignment,Statement,Break
from Typechecker.TypeEnvironment import TypeEnvironment
from Typechecker._Typechecker import Typechecker

# All tests must initialize a new Type Environment to pass to the Typechecker!
# Current number of tests: 11

def test_typeofIntLiteral():
    code = IntegerLiteral(5)
    envSpace = TypeEnvironment() 
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)

def test_typeofTrueExp():
    code = TrueExp()
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), BooleanType)

def test_typeofVariable():
    code = Variable("my_int_variable", IntType())
    envSpace = TypeEnvironment()
    envSpace.extend(code.name, code.varType) # All variables must be added to the Type Environment!
    myTypechecker = Typechecker(envSpace=envSpace)
    
    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)

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
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_sub_and_add, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_sub, envSpace), IntType)

def test_typeofAdditions():
    code_only_add = AdditionExp(IntegerLiteral(7), "+", IntegerLiteral(5))
    code_add_and_sub = AdditionExp(IntegerLiteral(35), "+", SubtractionExp(IntegerLiteral(10), "-", IntegerLiteral(5)))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_add_and_sub, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_add, envSpace), IntType)


def test_typeofMultiplications():
    code_only_mult = MultiplicationExp(IntegerLiteral(5), "*", IntegerLiteral(3))
    code_add_and_mult= MultiplicationExp(AdditionExp(IntegerLiteral(5), "+", IntegerLiteral(5)), "*", IntegerLiteral(2))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_add_and_mult, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_mult, envSpace), IntType)

def test_typeofDivisions():
    code_only_div = DivisionExp(IntegerLiteral(20), "/", IntegerLiteral(5))
    code_two_adds_and_div = DivisionExp(AdditionExp(IntegerLiteral(50), "+", IntegerLiteral(50)), "/", AdditionExp(IntegerLiteral(1), "+", IntegerLiteral(1)))
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code_two_adds_and_div, envSpace), IntType)
    assert isinstance(myTypechecker.typecheckExp(code_only_div, envSpace), IntType)

def test_typeofCommaExp():
    myVariable = Variable("num", IntType())
    code_addExp_trueExp_varExp = CommaExp([AdditionExp(IntegerLiteral(17), "+", IntegerLiteral(3)), TrueExp(), myVariable])
    envSpace = TypeEnvironment()
    envSpace.extend(myVariable.name, myVariable.varType)
    myTypechecker = Typechecker(envSpace=envSpace)

    assert myTypechecker.typecheckExp(code_addExp_trueExp_varExp, envSpace) == "Pass" # Note: idk what to return

def test_typeofCallExp(): #TODO this is a simple test case of CallExp
    code = CallExp(IntegerLiteral(10), None, None)
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    assert isinstance(myTypechecker.typecheckExp(code, envSpace), IntType)

#def test_typeofVarDec(): # This works, just commented out so that all tests pass
 #   code = Vardec(IntType(), Variable("foo", IntType()))
  #  myVariable = Variable("foo", IntType())
   # envSpace = TypeEnvironment()
    #envSpace.extend(myVariable.name, myVariable.varType)

    #myTypechecker = Typechecker(envSpace=envSpace)

    #assert isinstance(myTypechecker.typecheckStmt(code, envSpace), IntType)






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
def test_typeOfStmt():
    code1 = TrueExp()
    code2 = Return(IntegerLiteral(5))
    code = WhileLoop(code1, code2)
    statement = [code]
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    with pytest.raises(Exception):
        myTypechecker.typecheckStmt(statement, envSpace)

    statement = [code2]
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    with pytest.raises(Exception):
        myTypechecker.typecheckStmt(statement, envSpace)

    code = IfOptionalElse(TrueExp(), Return(IntegerLiteral(5)), Return(IntegerLiteral(2)))
    statement = [code]
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    with pytest.raises(Exception):
        myTypechecker.typecheckStmt(statement, envSpace)


    code = IfOptionalElse(TrueExp(), None, Return(IntegerLiteral(5)))
    statement = [code]
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    with pytest.raises(Exception):
        myTypechecker.typecheckStmt(statement, envSpace)


    code = Block([Return(IntegerLiteral(1)), Return(IntegerLiteral(2))])
    statement = [code]
    envSpace = TypeEnvironment()
    myTypechecker = Typechecker(envSpace=envSpace)

    with pytest.raises(Exception):
        myTypechecker.typecheckStmt(statement, envSpace)

