"""
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Peso da {i}º pessoa: "))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso foi de {maior}kg e o menor peso foi {menor} kg")