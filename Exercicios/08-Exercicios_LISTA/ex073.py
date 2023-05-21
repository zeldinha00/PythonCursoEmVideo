"""
     Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
     No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = []
maior = menor = 0

for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para posição {c}: ")))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print("=-" * 25)
print(f"Os numero digitados foi: {numeros}")
print(f"O \033[33mmaior\033[0;0m digitado foi \033[32m{maior}\033[0;0m nas posições ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"\033[33m{i}\033[0;0m... ", end="")
print()
print(f"O \033[33mmenor\033[0;0m digitado foi \033[32m{menor}\033[0;0m nas posições ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"\033[33m{i}\033[0;0m... ", end="")
print()
