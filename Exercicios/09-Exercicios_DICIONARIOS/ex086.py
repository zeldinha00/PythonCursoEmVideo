"""
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela.
"""
aluno = {}
sala = []

while True:
    aluno['nome'] = input("Nome do aluno: ")
    aluno['media'] = float(input(f"Media do aluno {aluno['nome']}: "))

    # tratamento para adicionar APROVADO OU REPROVADO
    if aluno['media'] >= 7:
        aluno['situacao'] = "Aprovado"
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = "Recuperação"
    else:
        aluno['situacao'] = "Reprovado"

    # tratamento para add alunos na sala
    sala.append(aluno.copy())

    # tratamento SAIDA do programa
    saida = input("Deseja continuar: [S/N]: ")
    if saida.lower() == 'n':
        break

for c in sala:
    for i in c.items():
        print(f"- {i[0]} é igual a {i[1]}")


