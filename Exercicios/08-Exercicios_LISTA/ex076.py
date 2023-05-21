"""
    Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    #Add numeros na lista
    lista.append(int(input("Digite um valor: ")))
    #tratamento S/N
    resp = str(input("Deseja continuar: [S/N]")).upper().strip()[0]
    if resp in "Nn":
        break

print(f"Foram digitados {len(lista)} numero na lista")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente {lista}")
if 5 in lista:
    print("Tem o numero 5 na lista")
else:
    print("Não tem o numero 5 na lista")

