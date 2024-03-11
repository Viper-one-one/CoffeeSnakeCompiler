import pytest
from Tokenizer.AdditionToken import AdditionToken

def test_equality():
    token1 = AdditionToken()
    token2 = AdditionToken()
    assert token1 == token2