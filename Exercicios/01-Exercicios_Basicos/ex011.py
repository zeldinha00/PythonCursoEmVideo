"""
    ### Faça um programa que leia o preço de um produto  e mostre seu novo preço com desconto de 5%.
"""

preco = float(input("Digite o valor do produto: R$ "))
desconto = preco - (preco * 5/100)   # foi calculado a porcentegem entre parentese depois subtraido pelo preço inicial
print(f"O produto no valor R${preco:.2f} agora tem 5% de valor e seu preço agora é R${desconto:.2f}")
