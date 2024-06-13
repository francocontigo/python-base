from decimal import Decimal

# mypy

produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5
cliente_especial = True


def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade

if cliente_especial:
    valor = Decimal(4.3)

total = calcula_total(valor, quantidade)
print(type(total))
print(total)
