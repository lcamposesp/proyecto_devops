import pytest

def contiene_letra(x,y):
    if x in y:
        return true
def test_contiene_letra():
    assert contiene_letra("C","Carlos") == True

def suma(x,y):
    return x+y

def test_suma():
    assert suma(11,10) > 5
