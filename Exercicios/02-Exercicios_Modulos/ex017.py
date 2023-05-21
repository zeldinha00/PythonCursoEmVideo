"""
    ### Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente:

    DICA: use a biblioteca math
"""
import math

angulo =  float(input("Digite o âgulo que você deseja: "))
print(f"""
O âgulo de {angulo} tem o SENO de {math.sin(math.radians(angulo)):.2f}
O âgulo de {angulo} tem o COCENO de {math.cos(math.radians(angulo)):.2f}
O âgulo de {angulo} tem o TANGENTE de {math.tan(math.radians(angulo)):.2f}
""")