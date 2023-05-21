"""
    Faça o jogo pedra - papel - tesoura, onde tem a opção do computador
"""
import random
import time
cores = {
    'limpa':'\033[m',
    'amarelo':'\033[1:33m',
    'verde':'\033[0:32m',
    'vermelho':'\033[0:31m'
}

itens = ("Pedra", "Papel", "Tesoura")

jogador = int(input("""Escola uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
opção => """))
computador = random.randint(0, 2)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
print(f"Computador:{cores['amarelo']}{itens[computador]}{cores['limpa']} Jogador:{cores['amarelo']}{itens[jogador]}{cores['limpa']}")
if computador == 0: # tratamento pedra
    if jogador == 0:
        print(f"Você {cores['amarelo']}EMPATOU{cores['limpa']}")
    elif jogador == 1:
        print(f"{cores['verde']}GANHOU{cores['limpa']}")
    elif jogador == 2:
        print(f"Você {cores['vermelho']}PERDEU{cores['limpa']}")
    else:
        print("OPÇÃO INVALIDA")
elif computador == 1: # tratamento papel
    if jogador == 0:
        print(f"Você {cores['vermelho']}PERDEU{cores['limpa']}")
    elif jogador == 1:
        print(f"{cores['amarelo']}EMPATOU{cores['limpa']}")
    elif jogador == 2:
        print(f"Você {cores['verde']}GANHOU{cores['limpa']}")
    else:
        print("OPÇÃO INVALIDA")
elif computador == 2: # tratamento tesoura
    if jogador == 0:
        print(f"Você {cores['vermelho']}PERDEU{cores['limpa']}")
    elif jogador == 1:
        print(f"{cores['verde']}GANHOU{cores['limpa']}")
    elif jogador == 2:
        print(f"Você {cores['amarelo']}EMPATOU{cores['limpa']}")
    else:
        print("OPÇÃO INVALIDA")

