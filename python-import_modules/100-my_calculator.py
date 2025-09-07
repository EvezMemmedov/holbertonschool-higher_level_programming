#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if operator == "+":
        result = add(a, b)
    if operator == "-":
        result = sub(a, b)
    if operator == "*":
        result = div(a, b)
    if operator == "/":
        result = mul(a, b)
    print(f"{a} {operator} {b} = {result}")
