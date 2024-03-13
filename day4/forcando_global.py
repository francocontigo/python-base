nome = "Global"

def funcao():
    nome = "Local"
    print("Nome local:", nome)
    nome = globals()["nome"]
    print("Nome Global:", nome)
    
funcao()