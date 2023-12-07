import sys

# EAFP - Easy to Ask Forgiveness than Permission
# É mais fácil pedir perdão que permissão

# try:
#     raise RuntimeError("Ocorreu um erro")
# except Exception as e:
#     print(str(e))


try:
    names = open("names.txt").readlines() # FileNotFoundError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"{str(e)}.") # Pode compor mensagens de erro
    sys.exit(1)
    # TODO: Usar retry
else: # Só ocorre quando não ocorre o erro
    print("Sucesso!")    
finally: # Sempre é executado, independente de ter erro ou não
    print("Sempre é executado")    
    
    
try:
    print(names[2])
except: # Bare Except
    print("[Error]: Missing name in the list")
    sys.exit(1)