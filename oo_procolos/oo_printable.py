# Protocolos / Data Model
# Printable

class Cor:
    english_name = "color"
    icon = "⬜"

    def __str__(self) -> str:
        return f"{self.english_name} - {self.icon}"


class Amarelo(Cor):
    english_name = "yellow"
    icon = "🟨"


class Azul(Cor):
    english_name = "blue"
    icon = "🟦"


class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"


print("casting")
obj = Amarelo()
new = str(obj) # casting
print(new)


print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())
