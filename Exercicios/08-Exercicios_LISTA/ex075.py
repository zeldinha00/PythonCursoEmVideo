"""
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
    já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []
for c in range(0, 5):
    numero = (int(input("Digite um valor: ")))
    if c == 0 or numero > lista[len(lista)-1]:
        lista.append(numero)
        print("Adicionado ao \033[33mfim\033[m da lista")
    else:
        posicoes = 0
        while posicoes < len(lista):
            if numero <= lista[posicoes]:
                lista.insert(posicoes, numero)
                print(f"Adicionado na \033[33m{posicoes}\033[m da lista.")
                break
            posicoes += 1
print("-=" * 28)
print(f"Os valores digitados em ordem foram \033[33m{lista}\033[m")