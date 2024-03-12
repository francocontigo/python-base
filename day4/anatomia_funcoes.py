# definição/atribuição
# assinatura + type hints
# docstring
# codigo
# valor de retorno, se não ter, vai retornar None

# -parametros
# posicional - passados em ordem
def nome_da_funcao(a: int, b: int, c: int) -> int:
    """Esta função soma a, b e c;

    Use está função quando quiser a + b + c
    
    >>> nome_da_funcao(1, 2, 3)
    6
    """
    return a + b + c

# passagem de argumentos posicionais -> quando se sabe o valor de um parametro
print(nome_da_funcao(1, 2, 3))

# passagem de argumentos nomeados
print(nome_da_funcao(c=3, b=2, a=1))

# passagem de argumentos mista, usa de forma posicional inicialmente e depois nomeada
print(nome_da_funcao(1, 2, c=3))



def outra_funcao(a, b, c):
    """Explicação da função"""
    # tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 = outra_funcao(1, 2, 3)
valores = outra_funcao(1, 2, 3)
valor, *resto = outra_funcao(1, 2, 3)



# Passagem de argumentos com desempacotamento
def soma(n1, n2):
    """Faz a soma de 2 numeros."""
    return n1 + n2

print(soma(10, 20))
# argumentos em sequencia / desempacota no modo posicional
args = (20, 30)
# print(soma(args[0], args[1]))
print(soma(*args))

# argumentos dicionário/nomeados
args = {"n2": 90, "n1": 100}  # dict, hasmap
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 10, "n1": 100},
    {"n2": 80, "n1": 120},
    (5, 10),
    {"n2": 93, "n1": 170},
    [29, 13],
    {"n2": 27, "n1": 82}
]
for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))