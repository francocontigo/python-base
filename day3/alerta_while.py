import logging

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

while True:
    if all(info.values()):
        break
    
    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)            
            break

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