# Exemplos de funções

from math import sqrt

"""
f(x) = 5 * (x / 2)
função f, com seu domínio x, após o = temos uma expressão, bloco que se espera retorno
"""


def f(x):  # assinatura -> nome e parametros
    return 5 * (x / 2)  # corpo da função


def f1(x):  # mesma coisa
    result = 5 * (x / 2)
    return result


def f2(x):
    return 5 * (x / 2)  # sem ter retorno, sempre retorna None


def double(x):
    return x * 2


valor = double(f(10))
print(valor)


# Funções sem retorno se chamam procedimentos/procedures
def print_in_upper(text):
    print(text.upper())
    # implicit return None


print_in_upper("ohayo")


def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def heron2(params):
    return heron(*params)


triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]
# aplique a função heron2 para cada elemento em triangulos
print(list(map(heron2, triangulos)))
for t in triangulos:
    # area = heron(t[0], t[1], t[2])
    # area = heron(*t)
    area = heron2(t)
    print(f"A area do triangulo é: {area}")
