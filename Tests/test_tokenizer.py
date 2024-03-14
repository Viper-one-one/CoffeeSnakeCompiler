import pytest
from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.Token import Token

def tokenizer(text):
    tokens = text.split()
    return tokens

def test_add_equality():
    token1 = AdditionToken()
    token2 = AdditionToken()
    assert token1 == token2
