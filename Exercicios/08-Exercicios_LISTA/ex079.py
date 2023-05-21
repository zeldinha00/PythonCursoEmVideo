pessoas = []
    #tratamento: menu
while True:
    print("*" * 40)
    opcao = input("""Selecione uma opção:
[1] - Cadastrar uma pessoa
[2] - Mostrar cadastrados
[3] - Mostrar maiores e menores de idade
[0] - Sair
opção-> """)
    print("*" * 40)
    #tratamento: cadastramento
    if opcao == "1":
        nome = input("Digite o nome: ").title().strip()
        idade = int(input("Digite a idade: "))
        pessoas.append((nome, idade))
    #tratamento: exibir cadastrados
    elif opcao == "2":
        for pessoa in pessoas:
            print(f"Nome: {pessoa[0]} / Idade: {pessoa[1]}")
    #tratamento: maior e menor de idade
    elif opcao == "3":
        for pessoa in pessoas:
            if pessoa[1] >= 18:
                print(f"{pessoa[0]} é maior de idade")
            else:
                print(f"{pessoa[0]} é menor de idade")
                print("-" * 40)
    #tratamento: finalizar programa
    elif opcao == "0":
        print("Obrigado por usar nosso sistema! VOLTE SEMPRE...")
        break
    #tratamento: validar opções
    else:
        print("Opção inválida. Por favor, digite novamente.")