"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

salvara as operações
"""
__version__ = "0.1.0"

import sys
import os
from datetime import datetime
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()    
log = logging.Logger(__name__, log_level) 
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)



while True:
    
    arguments = sys.argv[1:]
    
    # Validação
    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", 'div')
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            print(f"Numero inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)
        
    # TODO: Dicionário de funções
    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2

    path = os.curdir
    filepath = os.path.join(path, "calc.log")

    timestamp = datetime.now().isoformat()
    user= os.getenv("USER", "anonymous")

    print(f"O resultado é {result}")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        log.error(
            "%s",
            str(e)
        )
        sys.exit(1)

    print(f"O resultado é {result}")