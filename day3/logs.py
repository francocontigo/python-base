import os
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# TODO: usar função
# TODO: usar lib(loguru)
# normalmente o nome do script é usado, para setar o nível do logging é boa pratica usar a constante
log = logging.Logger(__name__, log_level) 
#level
# ch = logging.StreamHandler() # Streamhandler  = Console/terminal/stderr

# 10**6 = 1mb, backupCount=10 mantém os últimos arquivos(caso seja 1 vai apagaros mais antigos)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6, 
    backupCount=10
    ) 

# ch.setLevel(log_level)
fh.setLevel(log_level)
#formatacao, ver documentação para ver todas as mascaras
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
# log.addHandler(ch)
fh.setFormatter(fmt)
log.addHandler(fh)

log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios, informação atrelada ao sistema")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro que afeta todo o programa, ex: banco de dados sumiu")

print("---")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro: %s", str(e))

