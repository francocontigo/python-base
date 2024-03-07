__version__="0.1.1"

import os
import sys
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, "emails.txt")
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:
    
    for line in open(filepath):
        name, email = line.split()
        text = (open(templatepath).read() % {
            "nome": name, 
            "produto": "caneta", 
            "texto": "Boa qualidadeta!", 
            "link": "link", 
            "quantidade": 1, 
            "preco": 49.9
            }
        )
        
        from_ = "email@email.com"
        to = ", ".join([email])
        message = MIMEText(text, "html")
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to
    
        server.sendmail(from_, to, message.as_string())

