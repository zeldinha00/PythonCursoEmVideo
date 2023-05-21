"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Digite seu salario: "))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f"salario de R$ {salario} tem um aumento de 10%, salario novo é R$ {aumento:.2f}")
else:
    aumento = salario + (salario * 15 / 100)
    print(f"salario de R$ {salario} tem um aumento de 15%, salario novo é R$ {aumento:.2f}")