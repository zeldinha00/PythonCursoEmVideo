"""
    Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
    incluindo o total de gols feitos durante o campeonato.
"""
jogador = {}  # dicionario
partidas = []  # lista
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: ")).title()
    partidas_total = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    partidas.clear()
    for c in range(partidas_total):
        partidas.append(int(input(f"Quantos gols na partida {c+1}º: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input("Deseja continuar: [S/N]")).upper()[0]
        if resp in "SN":
            break
        else:
            print("Opção invalida digite S ou N.")
    if resp == "N":
        break

print("-" * 40)
print("cod", end=" ")
for i in jogador.keys():
    print(f"{i:<15}", end=" ")
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("-" * 40)

while True:
    busca = int(input("Buscar dado de qual jogador: (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERROR: não existe jogador com codigo {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}")
        for i, g in enumerate(time[busca]['gols']):
            print(f" no jogo {i+1} fez {g} gols. ")

