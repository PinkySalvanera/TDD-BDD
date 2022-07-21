import pytest

class Calculator:
    def add(self, a, b):
        return a + b
        
calc = Calculator()

def test_1():
    assert calc.add(1,1) == 2
    
def test_2():
    assert calc.add(1.0,2.5) == 3.5
    
def test_3():
    assert calc.add(0,0) == 0
    
def test_4():
    assert calc.add(-5,-6) == -11
    
print(calc.add(1, 1))    