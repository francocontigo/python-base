words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word:
        break
    
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter in "AEIOUaeiou":
            final_word += letter * 2
        else:
            final_word += letter
        # if ternario
        # final_word += letter * 2 if letter in "AEIOUaeiou" else letter
    words.append(final_word)

print(*words, sep="\n") # Desempacotamento=