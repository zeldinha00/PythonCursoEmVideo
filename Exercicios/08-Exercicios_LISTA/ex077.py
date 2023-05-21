"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
    respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input("Deseja continuar: [S/N]"))
    if resp in "Nn":
        break

print(f"Lista digitada:{lista}")
print(f"Os numeros pares são: {pares}")
print(f"Os numeros impares são: {impares}")