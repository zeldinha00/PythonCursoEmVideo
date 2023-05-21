"""
    Crie um programa onde o usuário possa digitar sete valores numéricos
    e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
    No final, mostre os valores pares e ímpares em ordem crescente.
"""
    # PAR [0]  [1] IMPAR
numeros = [[], []]

for i in range(7):
    numero = int(input(f"Digite {i + 1}º numero: "))

    if numero % 2 == 0:
        numeros[0].append(numero)  # Adiciona o número par à lista de números pares
    else:
        numeros[1].append(numero)  # Adiciona o número ímpar à lista de números ímpares

numeros[0].sort()  # Ordena os números pares em ordem crescente
numeros[1].sort()  # Ordena os números ímpares em ordem crescente

print(f"Pares: {numeros[0]}")
print(f"Pares: {numeros[1]}")
