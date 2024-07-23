import allure
import  pytest
def mult(x) :
    return  x*2

def test_sum1() :
    assert mult(3) == 6

def test_sum2():
        assert mult(2) == 6

def test_sum3():
        assert mult(4) == 8


#test_sum(2,4)