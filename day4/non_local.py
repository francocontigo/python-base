contador = 0

def funcao():
    global contador
    contador += 1 
    subcontador = 0
    def inner():
        global contador
        contador +=1

        nonlocal subcontador
        subcontador +=1
    inner()
    
funcao()
funcao()
print(globals())
print(contador)