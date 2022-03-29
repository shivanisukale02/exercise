import pytest
import Excercise

@pytest.mark.parametrize("num,output",[(23,True),(25,False)])
def test_prime(num,output):
    #x=23
    res=Excercise.prime(num)
    assert res==True

@pytest.mark.skip
def test_notPrime():
    x=25
    res=Excercise.prime(x)
    assert res==False


@pytest.mark.parametrize("num,output",[(12321,True),(21355,False)])
def test_palinderom(num,output):
    #x=12321
    res=Excercise.Palindrome(num)
    assert res==True

