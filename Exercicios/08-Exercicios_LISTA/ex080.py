"""
    Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
maior_peso = menor_peso = 0

while True:
    print("*" * 40)
    opcao = input("""Selecione uma opção:
[1] - Cadastrar uma pessoa
[2] - Mostrar cadastrados
[3] - Maior e Menor
[0] - Sair
opção-> """)
    print("*" * 40)

    if opcao == "1":
        nome = input("Digite o nome: ").title().strip()
        peso = float(input("Digite o peso: "))
        pessoas.append((nome, peso))

    elif opcao == "2":
        print(f"TOTAL CADASTRADO: {len(pessoas)}")
        for pessoa in pessoas:
            print(f"Nome: {pessoa[0]} / Peso: {pessoa[1]}")

    elif opcao == "3":
        if len(pessoas) > 0:
            maior_peso = max(pessoas, key=lambda x: x[1])[1]
            menor_peso = min(pessoas, key=lambda x: x[1])[1]
            maiores_pesos = [p[0] for p in pessoas if p[1] == maior_peso]
            menores_pesos = [p[0] for p in pessoas if p[1] == menor_peso]

            print("Pessoas com maior peso:")
            for pessoa in maiores_pesos:
                print(pessoa)

            print("\nPessoas com menor peso:")
            for pessoa in menores_pesos:
                print(pessoa)

            print("\nMaior peso: ", maior_peso)
            print("Menor peso: ", menor_peso)
        else:
            print("Nenhuma pessoa cadastrada.")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema! VOLTE SEMPRE...")
        break

    else:
        print("Opção inválida. Por favor, digite novamente.")
