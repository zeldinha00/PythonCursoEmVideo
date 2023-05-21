"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
    Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input("Informe seu sexo: [ M / F ]")).upper().strip()[0]
while sexo not in "MmFf":
    sexo = str(input("Opção invalida, favor entrar com o a opção valida: ")).upper().strip()[0]
print(f"Sexo {sexo} registrado com sucesso!!!")

