"""
Melhore o jogo do EX024 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
import random
computador = random.randint(0, 10)
tentativas = 0

print("== Jogo de advinhação -  tente acerta um número entre 0 e 10 ==")

while True:
    numero_escolhido = input("Escolha um numero: ")
    if numero_escolhido.isdigit():
        numero_escolhido = int(numero_escolhido)
        tentativas += 1
    else:
        print("ERROR: Favor inserir um numero inteiro!")
    if numero_escolhido == computador:
        print("Você Acertou!")
    else:
        if numero_escolhido > computador:
            print("Menos, tente um numero menor:")
        elif numero_escolhido < computador:
            print("Mais, tente um numero maior: ")
print(f"Você acertou com {tentativas} tentativas.")