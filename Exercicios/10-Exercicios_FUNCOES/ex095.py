import random

def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 10))
    return numeros

def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

# Sorteia os números
numeros_sorteados = sorteia()
print("Números sorteados:", numeros_sorteados)

# Calcula a soma dos números pares
soma_pares = somaPar(numeros_sorteados)
print("Soma dos números pares:", soma_pares)
