"""
    Crie um programa que simule o funcionamento de um caixa eletrônico.
    No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
    e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
    considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print("=" * 30)
print("{:^30}".format("BANCO ZEH"))
print("=" * 30)

valor = int(input("Qual o valor a ser secado: R$ "))
total = valor
cedula = 50
contador = 0
while True:
    if total >= cedula:
        total -= cedula
        contador += 1
    else:
        #tratamento para o print apenas das cedulas acima de 1
        if contador > 0:
            print(f"Total de cedulas {contador} de R$ {cedula:.2f}")
        #tratamento para cada cedula
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador = 0
        if total == 0:
            break
print("~" * 30)
print("{:^30}".format("VOLTE SEMPRE"))