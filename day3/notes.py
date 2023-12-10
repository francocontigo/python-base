""" Bloco de notas

$ notes.py new "Minha Nota"
tag: Minha tag
text:
Minha anotação

$ notes.py read Minha tag
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")


path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage!")
    print(f"you must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print("Invalid command {argument[0]}")

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        titulo, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {titulo}")
            print(f"text: {text}")
            print("-" * 30)
            print()
    
if arguments[0] == "new":
    # criacao nota
    try:
        titulo = arguments[1]
    except IndexError as e:
        print(f"[ERROR] {str(e)}")
        print("You need to pass more arguments.")
        
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

