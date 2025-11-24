from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide
from operations.modulus import modulus
from operations.power import power
from operations.squareroot import square_root

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(6, 2) == 12

def test_divide():
    assert divide(8, 2) == 4
    assert divide(5, 0) == "Error: Division by zero is not allowed."

def test_modulus():
    assert modulus(9, 4) == 1
    assert modulus(5, 0) == "Error: Modulus by zero is not allowed."

def test_power():
    assert power(2, 3) == 8

def test_square_root():
    assert square_root(16) == 4
    assert square_root(-1) == "Error: Cannot find square root of a negative number."

