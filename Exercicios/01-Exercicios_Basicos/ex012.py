"""
    ### Faça um programa que leia o salário do funcionario e mostre seu  novo salerio, com 15% de aumento.
"""
salario = float(input("Digite o salário do funcionário: R$ "))
novo_salario = salario + (salario * 15/100)
print(f"O salário de R${salario:.2f} com aumento de 15%, passa agora, para R${novo_salario:.2f}")
