import pytest

from Tokenizer.Lexer import Tokenizer
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
from Tokenizer.SubtractionToken import SubtractionToken
from Tokenizer.SuperToken import SuperToken
from Tokenizer.ThisToken import ThisToken
from Tokenizer.TrueToken import TrueToken
from Tokenizer.VoidToken import VoidToken
from Tokenizer.WhileToken import WhileToken

def testIdentifierEquals():
    token1 = IdentifierToken("foo")
    token2 = IdentifierToken("foo")
    assert token1 == token2

# use underscore to ignore function in test
def _testSingleToken(input_str: str, expected: Token):
    tokenizer = Tokenizer(input_str)
    tokens = tokenizer.tokenize()
    assert 1 == len(tokens) # check size of token array
    assert expected == tokens[0]

def testIf():
    _testSingleToken("if", IfToken())

# I don't like looking at errors so ignore for now
def _testIfWhitespaceAtEnd():
    _testSingleToken("if ", IfToken())

def testSingleDigitInteger():
    _testSingleToken("1", IntegerLiteralToken(1))

def testMultipleDigitInteger():
    _testSingleToken("123", IntegerLiteralToken(123))

def testTokenizeIdentifier():
    tokens = Tokenizer("bar").tokenize()
    expected = [IdentifierToken("bar")]
    assert expected == tokens

def testTokenizeVarDeclaration():
    tokens = Tokenizer("var x = 7").tokenize()
    expected = [VarToken(), IdentifierToken("x"), SingleEqualsToken(), IntegerLiteralToken(7)]
    assert expected == tokens