import logging
import time

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than Permission
# É mais fácil pedir perdão que permissão


def try_to_open_a_file(filepath, retry=1) -> list:
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    try:
        return open(filepath).readlines()  # FileNotFoundError
    except (FileNotFoundError, ZeroDivisionError) as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:  # Só ocorre quando não ocorre o erro
        print("Sucesso!")
    finally:  # Sempre é executado, independente de ter erro ou não
        print("Sempre é executado")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
