"""
    Crie um programa que leia nome, sexo e idade de várias pessoas,
    guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade
    C) Uma lista com as mulheres
    D) Uma lista de pessoas com idade acima da média
"""
dados = {}
lista = []
sum_idade = 0

while True:
    dados['nome'] = input("Nome: ").title()

    while True:
        dados['sexo'] = input("Sexo [M/F]: ")
        if dados['sexo'].upper() in ['M', 'F']:
            break
        else:
            print("Opção inválida. Digite 'M' para masculino ou 'F' para feminino.")

    dados['idade'] = int(input("Idade: "))
    sum_idade += dados['idade']
    lista.append(dados.copy())

    while True:
        sair = input("Deseja continuar? [S/N]: ").upper()[0]
        if sair in "SN":
            break
        else:
            print("Opção invalida digite S ou N.")
    if sair == "N":
        break

media_idade = sum_idade / len(lista)
print(lista)
print(f"total cadastrado {len(lista)}")
print(f"Media de idade é {media_idade:5.2f}")
print(f"As mulheres cadastrada foram: ", end=" ")
for p in lista:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']}", end=" ")
print()
print("Lista acima da media")
for p in lista:
    if p['idade'] >=media_idade:
        print("    ")
        for k, v in p.items():
            print(f"{k}, = {v},", end=" ")
print("<<< ENCERRADO >>>")