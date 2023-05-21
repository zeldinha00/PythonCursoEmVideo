"""
     Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
     5! = 5 x 4 x 3 x 2 x 1 = 120
"""
import math
numero = int(input("Escolha um número para calcular seu fatorial: "))
fatorial = math.factorial(numero)
contador = numero
print(f"Calculando {numero}!", end=" ")
while contador > 0:
    print(f"{contador} ", end='')
    print('x'if contador > 1 else '=', end=' ')
    contador -= 1
print(f"{fatorial}")
