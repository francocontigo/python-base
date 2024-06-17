from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List

# Enum
class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"


class ABCInstrument(ABC): # comportamento

    @abstractmethod
    def play(self): ...


@dataclass
class DataInstrumentMixin:  # deve ser usado junto com outra classe, dados
    name: str
    kind: str
    sound: InstrumentKind
    colors: List[str] = field(default_factory=list)


class Instrument(DataInstrumentMixin, ABCInstrument):
    ...


@dataclass
class Guitar(Instrument):
    n_strings: int = 6
    sound: str = "Ding ding ding"
    kind: InstrumentKind = InstrumentKind.string
    colors: List[str] = field(default_factory=lambda: ["red", "black"])

    def play(self):
        return self.sound


@dataclass
class ElectricGuitar(Guitar):
    sound: str = "Wah wah wah"

    def play(self, distortion=Distortion.wave):
        return_from_base_class = super().play() # mro, olha da esquerda para direita as importações
        if distortion == "wave":
            return "~~~~".join(return_from_base_class.split())
        if distortion == "whisper":
            return "...".join(return_from_base_class.split())
        return return_from_base_class



@dataclass
class Flute(Instrument):
    sound: str = "Flu flu flu"
    kind: InstrumentKind = InstrumentKind.wind
    colors: List[str] = field(default_factory=lambda: ["beige", "white"])

    def play(self):
        return self.sound
