from unnecessary_math import multiply

def test_numbers():
    assert multiply(3,4)==12

def test_strings():
    assert multiply('a',3)=='aaa'