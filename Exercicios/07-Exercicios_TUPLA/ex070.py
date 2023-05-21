"""
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
lista = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00,
         "Transferidor", 4.2,
         "Compasso", 9.99,
         "Mochila", 120.32)

print("-" * 40)
print(f"{'Listagem de Preços':^40}".upper())
print("-" * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end=" ")
    else:
        print(f"R${lista[pos]:>7.2f}")
