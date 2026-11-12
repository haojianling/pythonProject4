import pytest


def func(x):
    return x+3

def test_func():
    assert func(3)==5