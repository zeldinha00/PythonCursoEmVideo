"""
    Crie um programa que leia o ano de nascimento de sete pessoas.
    No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
import datetime
#contadores
menor = 0
maior = 0

for i in range(1, 8):
    data = int(input(f"Digite a {i}º data: "))
    idade = datetime.datetime.now().year - data
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} já atingiram a maior idade e {menor} ainda não são maior de idade.")

