from tabulate import tabulate

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    aluno = [nome, nota1, nota2]
    alunos.append(aluno)

# Criando uma tabela com o boletim
tabela = []
for i, aluno in enumerate(alunos, 1):
    id_aluno = i
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (nota1 + nota2) / 2
    tabela.append([id_aluno, nome, media])

# Exibindo o boletim em formato de tabela
print("\nBOLETIM")
print(tabulate(tabela, headers=["ID", "Nome", "Média"], tablefmt="grid"))

# Exibindo as notas individuais de um aluno específico
while True:
    opcao = input("\nDeseja ver as notas individuais de algum aluno? (s/n): ")
    if opcao.lower() == 'n':
        break

    numero_aluno = int(input("Digite o número do aluno: "))
    if 1 <= numero_aluno <= len(alunos):
        aluno = alunos[numero_aluno - 1]
        nome_aluno = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        print(f"Notas do Aluno {nome_aluno}: {nota1} e {nota2}")
    else:
        print("Número de aluno inválido.")

print("Encerrando o programa...")
