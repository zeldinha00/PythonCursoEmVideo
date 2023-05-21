"""
     Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
     Caso o número já exista lá dentro, ele não será adicionado.
     No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
numlist = []

while True:
    numero = int(input("Digite um númnero: "))
    if numero not in numlist:
        numlist.append(numero)
        print("Valor adiconado com sucesso")
    else:
        print("\033[33mValor duplicado não é adicionado\033[m")
    opcao = ' '
    while opcao not in "SN":
        opcao = str(input("Deseja continuar: [S/N]")).upper().strip()[0]
    if opcao == "N":
        break
numlist.sort()
print("-=" * 20)
print(f"A lista digita foi: \033[33m{numlist}\033[m")
