import pytest

from Tokenizer._Lexer import Tokenizer
from Tokenizer.Token import Token
from Tokenizer.VarToken import VarToken
from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.BreakToken import BreakToken
from Tokenizer.ClassToken import ClassToken
from Tokenizer.CommaToken import CommaToken
from Tokenizer.DivisionToken import DivisionToken
from Tokenizer.DotToken import DotToken
from Tokenizer.ElseToken import ElseToken
from Tokenizer.ExtendsToken import ExtendsToken
from Tokenizer.FalseToken import FalseToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.IfToken import IfToken
from Tokenizer.InitToken import InitToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
from Tokenizer.IntToken import IntToken
from Tokenizer.LeftCurlyBraceToken import LeftCurlyBraceToken
from Tokenizer.LeftParenToken import LeftParenToken
from Tokenizer.MethodToken import MethodToken
from Tokenizer.MultiplicationToken import MultiplicationToken
from Tokenizer.NewToken import NewToken
from Tokenizer.PrintlnToken import PrintlnToken
from Tokenizer.ReturnToken import ReturnToken
from Tokenizer.RightCurlyBraceToken import RightCurlyBraceToken
from Tokenizer.RightParenToken import RightParenToken
from Tokenizer.SemiColonToken import SemiColonToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.StringLiteralToken import StringLiteralToken
from Tokenizer.SubtractionToken import SubtractionToken
from Tokenizer.SuperToken import SuperToken
from Tokenizer.ThisToken import ThisToken
from Tokenizer.TrueToken import TrueToken
from Tokenizer.VoidToken import VoidToken
from Tokenizer.WhileToken import WhileToken
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
from Parser.TypesAndNames.ClassName import ClassName
from Parser.TypesAndNames.MethodName import MethodName
from Parser.Vardec import Vardec
from Parser._Parser import Parser
from Parser.PrimaryExp import Variable
from Parser.PrimaryExp import StringLiteral
from Parser.PrimaryExp import IntegerLiteral
from Parser.PrimaryExp import ThisExp
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import NewObjectExp
from Parser.AddExp import AdditionExp
from Parser.AddExp import SubtractionExp
from Parser.MultExp import MultiplicationExp
from Parser.MultExp import DivisionExp
from Parser.CommaExp import CommaExp
from Parser.CommaVardec import CommaVardec
from Parser.CallExp import CallExp
from Parser.Statement import Assignment
from Parser.Statement import WhileLoop
from Parser.Statement import Break
from Parser.Statement import Return
from Parser.Statement import IfOptionalElse
from Parser.Statement import Block


# def testClassDefWithExtends():
#     code = """
#             class Animal extends Boom {
#             init() {}
#             method speak() Void { return println(0); }
#             }
#            """
#     tokenizer = Tokenizer(code)
#     tokens = tokenizer.tokenize()
#     # print("Tokens", tokens)
#     parser = Parser(tokens)
#     classdef = parser.parse_classdef()


def testVardec():
    code = [IntToken(), IdentifierToken("x")]
    parser = Parser(code)
    vardec = parser.vardec_parse()
    
    expected_vardec = Vardec(IntType, Variable("x", IntType))
    
    assert expected_vardec.varType == vardec.varType
    assert expected_vardec.var.name == vardec.var.name
    assert expected_vardec.var.varType == vardec.var.varType

# will need to take this out
def testPrimaryString():
    code = [StringLiteralToken("hello")]
    parser = Parser(code)
    string_exp = parser.primary_exp_parse()

    expected_string = StringLiteral("hello")
    assert expected_string == string_exp

def testPrimaryInt():
    code = [IntegerLiteralToken(2)]
    parser = Parser(code)
    int_exp = parser.primary_exp_parse()

    expected_int = IntegerLiteral(2)
    assert expected_int == int_exp

def testPrimarySingleExp():
    code = [ThisToken()]
    parser = Parser(code)
    single_exp = parser.primary_exp_parse()

    expected_exp = ThisExp()
    assert expected_exp == single_exp

def testNewObjectExp():
    code = [NewToken(), IdentifierToken("classname"), LeftParenToken(), IntegerLiteralToken(2), CommaToken(), IdentifierToken("one"), RightParenToken()]
    parser = Parser(code)
    new_exp = parser.primary_exp_parse()

    expected_exp = NewObjectExp(
        IdentifierToken("classname"), 
        CommaExp([IntegerLiteral(2), Variable("one")])
    )
    assert new_exp == expected_exp


def testCommaExp():
    code = [
    IntegerLiteralToken(2), 
    CommaToken(), 
    TrueToken(), 
    CommaToken(), 
    ThisToken()
    ] # 2, true, this
    parser = Parser(code)
    comma_exp = parser.comma_exp_parse()

    expected_exp = CommaExp([
        IntegerLiteral(2), 
        TrueExp(), 
        ThisExp()
    ])

    assert comma_exp == expected_exp

def testAddExp():
    input_string = "2 + 3 - 1"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    add_exp = parser.add_exp_parse()

    expected_exp = SubtractionExp(AdditionExp(IntegerLiteral(2), "+", IntegerLiteral(3)), "-", IntegerLiteral(1))

    assert add_exp == expected_exp


def testMultExp():
    input_string = "2 * 3 / 1"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    mult_exp = parser.mult_exp_parse()

    expected_exp = DivisionExp(MultiplicationExp(IntegerLiteral(2), "*", IntegerLiteral(3)), "/", IntegerLiteral(1))

    assert mult_exp == expected_exp

def testCallExp():
    input_string = "cat.speak(2, one)"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    call_exp = parser.call_exp_parse()
    expected_exp = CallExp(Variable("cat"), MethodName("speak"), CommaExp([IntegerLiteral(2), Variable("one")]))

    assert call_exp == expected_exp

def testAssignment():
    input_string = "ball = 2;"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    assign_exp = parser.statement_parse()
    expected_exp = Assignment(IntegerLiteral(2), Variable("ball"))

    assert assign_exp == expected_exp

def testWhileLoop():
    input_string = """while (true) x = x + 1;"""
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    while_exp = parser.while_parse()
    expected_exp = WhileLoop(TrueExp(), Assignment(AdditionExp(Variable("x"), "+", IntegerLiteral(1)), Variable("x")))
    
    print("while", while_exp)
    print("expected", expected_exp)

    assert while_exp == expected_exp

def testBreak():
    input_string = "break;"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    break_exp = parser.statement_parse()
    expected_exp = Break()

    assert break_exp == expected_exp

def testReturnVoid():
    input_string = "return;"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    return_stmt = parser.return_parse()
    expected_stmt = Return(None)

    assert return_stmt == expected_stmt

def testReturnExpression():
    input_string = "return x;"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    return_stmt = parser.return_parse()
    expected_stmt = Return(Variable("x"))

    assert return_stmt == expected_stmt

def testIfStatement():
    input_string = "if (true) x = 1;"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    if_stmt = parser.if_parse()
    expected_stmt = IfOptionalElse(TrueExp(), Assignment(IntegerLiteral(1), Variable("x")), None)

    assert if_stmt == expected_stmt

def testIfStatementWithElse():
    input_string = "if (true) x = 1; else x = 2;"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    if_stmt = parser.if_parse()
    expected_stmt = IfOptionalElse(TrueExp(), Assignment(IntegerLiteral(1), Variable("x")), Assignment(IntegerLiteral(2), Variable("x")))

    assert if_stmt == expected_stmt

def testBlockStatement():
    input_string = "{x = 1; x = 2;}"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    block_stmt = parser.block_parse()
    expected_stmt = Block([Assignment(IntegerLiteral(1), Variable("x")), Assignment(IntegerLiteral(2), Variable("x"))])

    assert block_stmt == expected_stmt

def testCommaVardec():
    input_string = "Int x, Boolean z, Int y"
    tokenizer = Tokenizer(input_string)
    code = tokenizer.tokenize()
    parser = Parser(code)

    commavardec_stmt = parser.comma_vardec_parse()
    expected_stmt = CommaVardec([Vardec(IntType, Variable("x", IntType)), Vardec(BooleanType, Variable("z", BooleanType)), Vardec(IntType, Variable("y", IntType))])

    print("commavardec", commavardec_stmt)
    print("expected", expected_stmt)

    assert commavardec_stmt == expected_stmt