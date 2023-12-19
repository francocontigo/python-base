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

while True:
    
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?"). strip().lower()
            
        for line in open(filepath):
            titulo, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {titulo}")
                print(f"text: {text}")
                print("-" * 30)
                print()
        
    if arguments[0] == "new":
        try:
            titulo = arguments[1]
        except IndexError as e:
            titulo = input("Qual é o titulo?"). strip().title()
            
        text = [
            f"{titulo}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
        # \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    
    cont = input("Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
    if cont != "y":
        break

