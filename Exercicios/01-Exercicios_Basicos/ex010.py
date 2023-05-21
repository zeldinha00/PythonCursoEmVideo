"""
  ### Faça um programa que leia a largura e altura  de uma parede em metros, calcule sua area e a
    quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
"""

largura =  float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da pararede: "))

area = largura * altura
litros = area / 2

print(f"A área é de {area}m² e você vai precisar usar {litros} litros de tinta.")