from instruments import Instrument, Guitar, Flute, ElectricGuitar, Distortion

# x = Instrument()

gianini = Guitar("Gianini m2", colors=["green"])
print(gianini.play())
print(gianini.colors)


yamaha = Flute("Yamaha Magic Flute", colors=["silver"])
print(yamaha.play())
print(yamaha.colors)

lespaul = ElectricGuitar("lespaul m1")
print(lespaul.play(distortion=Distortion.whisper))
