"""
    Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
def area(larg, comp):
    area = larg * comp
    print(f"A area de um terreno {larg}m x {comp}m é de {area}m²")


print("Controle de terreno")
print("*" *20)
l = float(input("Largura: "))
c = float(input("Altura: "))
area(l, c)
