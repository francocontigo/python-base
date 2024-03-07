"""
    Exemplo de envio de e-mail
"""

import smtplib

SERVER = "localhost"
PORT = 8025

# Dados Email
FROM = "sgidodos@gmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "E-mail via Python"
TEXT = """\
Testando email via Python
<b>É pra ter ficado em negrito<b>
"""

# Existe outros metadas mas esses dados são obrigatórios, \ é pra evitar a primeira quebra de linha
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

# python -m smtpd -c DebuggingServer -n localhost:8025
with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
    
    