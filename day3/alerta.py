import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

for key in info.keys():
    try:
        info[key] = float(input(f"Qual a {key} atual? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} invalida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

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