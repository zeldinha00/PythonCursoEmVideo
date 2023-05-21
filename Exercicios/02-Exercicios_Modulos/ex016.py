"""
    ### Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um triagulo retangulo ,
    calcule e mostre o comprimento da hipotenusa

    DICA: use a biblioteca math
"""
import math
co= float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
## modo2: math.sqrt((math.pow(co, 2) + math.pow(ca, 2)))
## modo3: (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa do tringulo vai medir {hi:.2f}")
