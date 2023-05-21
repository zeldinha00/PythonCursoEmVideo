"""
    ###Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu.

    DICA: biblioteca random
"""
import random
import time
computador = random.randint(0, 5) # computador pensar no numero
print(f"{'':=^52}")
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print(f"{'':=^52}")

escolhido = int(input("Que número eu pensei? "))  # numero escolhido pelo jogador
print("PROCESSANDO...")
time.sleep(2)

if escolhido == computador:
    print(f"Número que pensei foi {computador} - Acertou")
else:
    print(f"Número que pensei foi {computador} - ERROU")
