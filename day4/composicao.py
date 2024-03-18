names = [
    "Bruno",
    "João",
    "Bernardo",
    "Barbara",
    "Brian",
]

# estilo funcional
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()


# estilo procedural
def starts_with_b(text):
    return text[0].lower


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
