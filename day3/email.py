__version__="0.1.1"

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, "emails.txt")
templatepath = os.path.join(path, templatename)

clientes = []
for line in open(filepath):
    name, email = line.split()
    clientes.append(line.split(","))
    
    # TODO Substituir por envio de email
    print(f"Enviando email para {email}")
    print()
    print(open(templatepath).read() % {"nome": name, "produto": "caneta", "texto": "Boa qualidadeta!",
     "link": "link", "quantidade": 1, "preco": 49.9})
    print("-" * 50)
