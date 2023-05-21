"""
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num1 = 5 % 2
print(num1)
total = 0
num = int(input("Digite um valor: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(f"\033[33m", end=" ")
        total += 1
    else:
        print(f"\033[31m", end=" ")
    print(f"{i}", end=" ")
print(f"\n\033[mO número {num} foi divisível {total} vezes")
if total == 2:
    print("Número PRIMO")
else:
    print("NÃO é PRIMO")
