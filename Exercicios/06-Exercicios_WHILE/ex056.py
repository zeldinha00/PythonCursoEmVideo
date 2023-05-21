"""
    Refaça o DESAFIO EX046, lendo o primeiro termo e a razão de uma PA,
    mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print("=" * 30)
print(f"Gerador de uma PA".upper())
print("=" * 30)
primeiro = int(input("Primeiro termo:"))
razao = int(input("Razão: "))
termo = primeiro
contador = 1

while contador <= 10:
    print(f"{termo}", end=" ")
    print("=>" if contador < 10 else " ", end=" ")
    termo += razao
    contador += 1
