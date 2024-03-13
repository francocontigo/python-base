# escopo global
nome = "Global"
numero = 1
flag = True

def funcao():
    # escopo local
    nome = "Local"
    
    def inner_function(): # também chamado de closure
        # escopo local da inner
        nome = "Interna"
        print(nome)
        return nome
        # fim escopo inner
    
    print("Escopo local: ", locals())
    print()
    inner_function()
    print(nome)
    print()
    return nome
    # fim escopo local

print()
print("Escopo Global do programa: ", globals())
funcao()
print(nome)
# fim escopo global