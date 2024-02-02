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

print(info["temperatura"])
print(info["umidade"])