"""
    Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato
"""

print("=" * 25)
print("{:^25}".format("SUPERMERCADO ZELDINHA"))
print("=" * 25)

total = mais_mill = menor = cont = 0
barato = ''
while True:
    produto = str(input("Nome do produto: "))
    valor = float(input("Valor do produto: "))
    cont += 1
    total += valor
    if valor > 1000:
        mais_mill += 1
    new = ' '
    while new not in "SN":
        new = str(input("Quer continuar: [S/N]: ")).upper().strip()[0]
    if new == "N":
        break
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto

print("=" * 25)
print("{:^25}".format("FIM DAS COMPRAS"))
print("=" * 25)
print(f"""Valor total das compras: R$ {total:.2f}
Tem {mais_mill} produtos acima de R$ 1.000,00
O Produto mais barato é {barato} no valor de R$ {menor:.2f}
""")