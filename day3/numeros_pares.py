"""
Programa que imprime os números pares de 1 a 200

ex:
'python numeros_pares.py'
2
4
6
8
"""

for num in range(0,201,2):
    print(num)
    
for num in range(1,201):
    if num % 2 != 0:
        continue
    print(num)
    
    