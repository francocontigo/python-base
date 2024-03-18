def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)


names = ["Bruno", "João", "Bernardo", "Amanda", "Ana", "Julia"]

print(sorted(names, key=lambda name: name.count("a")))

print(list(filter(lambda name: name[0].lower() == "b", names)))

print(list(map(lambda name: "Hello " + name, names)))

# Calculadora
operacao = input("operacao [sum, num, div, sub]: ").strip()
n1 = int(input("n1: ").strip())
n2 = int(input("n2: ").strip())

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

print(f"O resultado é: {operacoes[operacao](n1, n2)}")