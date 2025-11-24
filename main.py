from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide
from operations.modulus import modulus
from operations.power import power
from operations.squareroot import square_root
from utils.input_handler import read_float, read_choice

MENU = """
=== PYTHON BASIC CALCULATOR ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Square Root
0. Exit
"""

def main():
    print("Welcome to Basic Python Calculator")
    while True:
        print(MENU)
        choice = read_choice("Enter choice (0–7): ", [str(i) for i in range(0, 8)])

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "7":
            num = read_float("Enter number: ")
            print("Result:", square_root(num))
            continue

        a = read_float("Enter first number: ")
        b = read_float("Enter second number: ")

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", modulus(a, b))
        elif choice == "6":
            print("Result:", power(a, b))

if _name_ == "_main_":
    main()


