# __add__ / __radd__


class Cor:
    icon = "⬜"
    def __str__(self) -> str:
        return f"{self.icon}"

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


print("Cores primárias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()

print(vermelho, amarelo, azul)

print("Cores secundárias")
print(amarelo + vermelho) # Tipagem Forte, náo tenta coerção
print(azul + amarelo)
print(vermelho + azul)
