"""
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
    O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
    cadastrando tudo em uma lista composta.
"""
import random
import time

num_jogos = int(input("Quantos jogos deseja realizar: "))

jogos = []
for i in range(num_jogos):
    jogo = []
    for i in range(6):
        numero = random.randint(1, 60)
        jogo.append(numero)
    jogos.append(jogo)


# Exibindo os jogos gerados
print(f"{f' Gerando os {num_jogos} jogos: ':=^33}")
for i, jogo in enumerate(jogos):
    jogo.sort()
    time.sleep(1)
    print(f"{i+1}º jogo: {jogo}")
print(f"{'< BOA SORTE >':=^33}")
