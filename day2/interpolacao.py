email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Ricardo"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "Boa qualidadeta!",
     "link": "link", "quantidade": 1, "preco": 49.9})
