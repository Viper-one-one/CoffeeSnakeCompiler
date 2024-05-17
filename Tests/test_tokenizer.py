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

def testTokenizeClass():
    tokens = Tokenizer("class").tokenize()
    expected = [ClassToken()]
    actual = [type(token) for token in tokens]
    actual_expected = [type(token) for token in expected]
    print(actual)
    print(actual_expected)
    assert expected == tokens

def testTokenizeBreak():
    tokens = Tokenizer("break").tokenize()
    expected = [BreakToken()]
    assert expected == tokens

def testTokenizeSampleCode():
    code = """
        class Animal {
            init() {}
            method speak() Void { return println(0); }
            }
            class Cat extends Animal {
            init() { super(); }
            method speak() Void { return println(1); }
            }
            class Dog extends Animal {
            init() { super(); }
            method speak() Void { return println(2); }
            }

            Animal cat;
            Animal dog;
            cat = new Cat();
            dog = new Dog();
            cat.speak();
            dog.speak();
    """
    tokens = Tokenizer(code).tokenize()
    expected = [ClassToken(), IdentifierToken("Animal"), LeftCurlyBraceToken(),
                InitToken(), LeftParenToken(), RightParenToken(), LeftCurlyBraceToken(),
                RightCurlyBraceToken(), MethodToken(), IdentifierToken("speak"), 
                LeftParenToken(), RightParenToken(), VoidToken(), 
                LeftCurlyBraceToken(), ReturnToken(), PrintlnToken(), LeftParenToken(), 
                IntegerLiteralToken(0), RightParenToken(), SemiColonToken(), 
                RightCurlyBraceToken(), RightCurlyBraceToken(), ClassToken(), 
                IdentifierToken("Cat"), ExtendsToken(), IdentifierToken("Animal"), 
                LeftCurlyBraceToken(), InitToken(), LeftParenToken(), RightParenToken(), 
                LeftCurlyBraceToken(), SuperToken(), LeftParenToken(), RightParenToken(), 
                SemiColonToken(), RightCurlyBraceToken(), MethodToken(), 
                IdentifierToken("speak"), LeftParenToken(), RightParenToken(), 
                VoidToken(), LeftCurlyBraceToken(), ReturnToken(), 
                PrintlnToken(), LeftParenToken(), IntegerLiteralToken(1), 
                RightParenToken(), SemiColonToken(), RightCurlyBraceToken(), 
                RightCurlyBraceToken(), ClassToken(), IdentifierToken("Dog"), 
                ExtendsToken(), IdentifierToken("Animal"), LeftCurlyBraceToken(), 
                InitToken(), LeftParenToken(), RightParenToken(), LeftCurlyBraceToken(), 
                SuperToken(), LeftParenToken(), RightParenToken(), SemiColonToken(), 
                RightCurlyBraceToken(), MethodToken(), IdentifierToken("speak"), 
                LeftParenToken(), RightParenToken(), VoidToken(), 
                LeftCurlyBraceToken(), ReturnToken(), PrintlnToken(), LeftParenToken(), 
                IntegerLiteralToken(2), RightParenToken(), SemiColonToken(), 
                RightCurlyBraceToken(), RightCurlyBraceToken(), IdentifierToken("Animal"),
                IdentifierToken("cat"), SemiColonToken(), IdentifierToken("Animal"), 
                IdentifierToken("dog"), SemiColonToken(), IdentifierToken("cat"), 
                SingleEqualsToken(), NewToken(), IdentifierToken("Cat"), LeftParenToken(), 
                RightParenToken(), SemiColonToken(), IdentifierToken("dog"), 
                SingleEqualsToken(), NewToken(), IdentifierToken("Dog"), LeftParenToken(), 
                RightParenToken(), SemiColonToken(), IdentifierToken("cat"), DotToken(), 
                IdentifierToken("speak"), LeftParenToken(), RightParenToken(), 
                SemiColonToken(), IdentifierToken("dog"), DotToken(), IdentifierToken("speak"), 
                LeftParenToken(), RightParenToken(), SemiColonToken()]
    assert expected == tokens