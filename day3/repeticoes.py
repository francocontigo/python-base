#numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1, 11) # inicial, final, passo

print(numbers[-1])
print(numbers[2:])

for number in numbers:
    par = number % 2 == 0
    if number == 9:
        break # interrompe a execução
    elif par:
        print(number)
    else:
        continue # retorna para o loop sem executar o bloco de código abaixo
    
    print(f"mais codigo com {number}")

#  Funcional
original = [1, 2 , 3]

# Laço for de forma estruturada
# dobrada = []
# for n in original:
#     dobrada.append(n * 2)
# print(dobrada)
    
# list comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# dict comprehension
dados = {number for number in original if number < 3}
print(dados)