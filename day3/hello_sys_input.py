"""Hello World Multi Linguas.
Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.
Como usar:
Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR
Execução:
    python hello.py
    ou
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.2.0"
__author__ = "Ricardo Franco"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()    
log = logging.Logger(__name__, log_level) 
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value = value.strip()
    
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language =  current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

"""
# Try com valor default
message = msg.get(current_language, msg["en_US"])
"""

# EAPF
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language: {current_language} is invalid!")
    print(f"Choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))

