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
    code = [IntToken(), IdentifierToken("x"), SemiColonToken()]
    parser = Parser(code)
    vardec = parser.vardec_parse()
    
    expected_vardec = Vardec(IntType, Variable("x", IntType))
    
    assert expected_vardec.varType == vardec.varType
    assert expected_vardec.var.name == vardec.var.name
    assert expected_vardec.var.varType == vardec.var.varType

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

def testPrimarySingleToken():
    code = [ThisToken()]
    parser = Parser(code)
    single_exp = parser.primary_exp_parse()

    expected_exp = ThisExp()
    assert expected_exp == single_exp