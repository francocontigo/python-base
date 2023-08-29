"""Exibe o relatório de crianças por atividade.

Imprimir a lista de crianças agrudaoadas por sala 
que frequentam cada uma das atividades.
"""
__version__= "0.3.0"

# Dados
salas = {"Sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
         "Sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "Ingles": ["Erick", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

aulas_por_sala = {}

# Listar alunos em cada atividade por sala
for sala, alunos in salas.items():
    for aula, alunos_aula in aulas.items():
        alunos_atividade = []
        for aluno in alunos:
            if aluno in alunos_aula:
                alunos_atividade.append(aluno)
        aulas_por_sala[f"{sala} {aula}"] = alunos_atividade
        

for atividade_sala, alunos in aulas_por_sala.items():
    print(f"{atividade_sala}:")
    for aluno in alunos:
        print(f"- {aluno};")
    print("-" * 32)
