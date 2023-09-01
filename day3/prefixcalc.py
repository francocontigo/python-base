"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

arguments = {
    "operation": None,
    "n1": None,
    "n2": None
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    arguments[key] = value
    
operation, n1, n2 = arguments.values()

if operation == "sum":
    print(f"{n1} + {n2} = {int(n1) + int(n2)}")
elif operation == "sub":
    print(f"{n1} - {n2} = {int(n1) - int(n2)}")
elif operation == "mul":
    print(f"{n1} * {n2} = {int(n1) * int(n2)}")
elif operation == "div":
    print(f"{n1} / {n2} = {int(n1) / int(n2)}")
else:
    print(f"Invalid Operation! {arguments['operation']}")