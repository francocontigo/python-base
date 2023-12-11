# Pseudo Código
import ir, pegar, pedir, tem, comer, ficar

# Premissas
dia = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriados = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
if dia in feriados and  not natal:
    padaria_aberta = False
elif (dia not in semana and hora < horario_padaria["fds"]):
    padaria_aberta = True
elif dia in semana and hora < horario_padaria["semana"]: # poderia ser unido com or com a condicional acima.
    padaria_aberta = True
else:
    padaria_aberta = False
    
if padaria_aberta is True: # se compara com is e nõa ==, poderia ser só if padaria_aberta
    if chovendo and (frio or nevando): # não precisa dos parenteses, precedência pelo lado direito
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("água")
    elif chovendo:
        pegar("guarda-chuva")

    ir("padaria")

    if tem("pão integral") and tem("baguete"):
        pedir(6, "pão integral")
        pedir(6, "baguete")
    elif tem("pão integral") or tem("baguete"):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "o que tiver")
else:
    ficar("casa")
    comer("Bolacha")
    
        