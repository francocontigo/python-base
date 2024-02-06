import sys
import logging

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO: Decimal
            "disponivel" : True
        }
except FileNotFoundError:
    logging.error("Arquivo não encontrado")
    sys.exit(1)
    
for codigo, dados in quartos.items:
    nome = dados["nome"]
    preco = dados["preco"]
    #disponivel = "🚫" if not dados["disponivel"] else "👍"
    disponivel = dados["disponivel"] and "👍" or "🚫" # retorno com and é sempre o último avaliado
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")

nome = input("Nome do cliente:").strip()
quarto = int(input("Número do quarto").strip())