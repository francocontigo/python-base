import sys
import logging

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe.")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO: Decimal
            "disponivel" : False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe.")
    sys.exit(1)

if len(ocupados) == len(quartos):
    print("Hotel lotado.")
    sys.exit(1)

print("Reserva Hotel Pythonico")
print("-" * 40)
print("Lista de quartos disponíveis:")
for codigo, dados in quartos.items:
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "🚫" if not dados["disponivel"] else "👍"
    #disponivel = dados["disponivel"] and "👍" or "🚫" # retorno com and é sempre o último avaliado
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")

print("-" * 40)
nome = input("Nome do cliente:").strip()
try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponível"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido!")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Quantos dias? ").strip())
except ValueError:
    logging.error("Número inválido!")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")
