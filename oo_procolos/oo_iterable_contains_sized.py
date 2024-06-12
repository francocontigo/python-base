# Iterable - __iter__

# nome = "Ricardo" # str
# for letra in nome:
#     print(letra)

# print(list(nome))


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

    def __len__(self):
        return 2


class Vermelho(Cor):
    icon = "🟥"

    def __len__(self):
        return 1


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"

    def __len__(self):
        return 3


class Violeta(Cor):
    icon = "🟪"


# Iterable(__iter__) e container(__contains__) e sized(__len__) e Subscritable()
# é considerado collection quem tem: Sized + Container + Iterable
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor for cor in self._cores])

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):  # 0, 2::4
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())

for cor in rgb:
    print(cor)

print("🟥" in rgb)

for cor in rgb:
    print(cor, len(cor))

print(len(rgb))

print(rgb[0])

print(rgb["azul"])

class Thing:
    ...

print(dir(Thing))
print()
print(dir(object))
t = Thing()
print(t)

t.valor = 10 # __setattr__
print(t.valor) # __ getattr__

del t.valor # __delattr__
print(t.valor) # __getattribute__ -> quando não encontra oa atributo

print(dir(t)) # __dir__
