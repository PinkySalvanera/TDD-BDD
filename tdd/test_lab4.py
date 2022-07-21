import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b

@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    assert True
    

def test_lab4_1(base_calculator):
    assert base_calculator.subtract(7,2) == 5
        
def test_lab4_2(base_calculator):        
    assert base_calculator.subtract(2,5) == -3
        
def test_lab4_3(base_calculator):        
    assert base_calculator.subtract(2.5,1) == 1.5
        
def test_lab4_4(base_calculator):        
    assert base_calculator.subtract(-2.5,-1) == -1.5        
        
def test_lab4_5(base_calculator):
    assert base_calculator.multiply(3,9) == 27
    
def test_lab4_6(base_calculator):
    assert base_calculator.multiply(-3,9) == -27    
    
def test_lab4_7(base_calculator):
    assert base_calculator.multiply(2.5,1) == 2.5
    
def test_lab4_8(base_calculator):
    assert base_calculator.multiply(-2.5,-1) == 2.5
        
