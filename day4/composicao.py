names = ["Bruno", 
         "João", 
         "Bernardo", 
         "Barbara", 
         "Brian",
]

# for name in names:
#     if name.lower().startswith("b"):
#         print(name)

# TODO: Usar lambdas

def starts_with_b(text):
    return text[0].lower() == "b"
    #return text.lower().startswith("b")

print(*list(filter(starts_with_b, names)))