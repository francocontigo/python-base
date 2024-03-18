import logging
from typing import Dict

log = logging.Logger("alerta")

# TODO: Mover para módulo de utilidades.


def is_completely_filled(dict: Dict) -> bool:
    """Return a boolean telling if a dict is completely filled."""
    info_size = len(dict)
    filled_size = len([value for value in dict.values() if value is not None])
    return info_size == filled_size


def read_inputs_for_dict(dict: Dict):
    """Reads information for a dict from user input."""
    for key in dict.keys():
        if dict[key] is not None:
            continue
        try:
            dict[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break


info = {"temperatura": None, "umidade": None}

while not is_completely_filled(info):
    read_inputs_for_dict(info)

temp, umidade = info.values()

if temp > 45:
    print("ALERTA!!! Perigo de calor extremo!")
elif temp * 3 >= umidade:
    print("ALERTA!!! Perigo de calor umido!")
elif temp >= 10 and temp <= 30:
    print("Temperatura normal!")
elif temp >= 0 and temp < 10:
    print("Frio!")
elif temp < 0:
    print("ALERTA!!! Frio Extremo!")
else:
    print("Calor!")
