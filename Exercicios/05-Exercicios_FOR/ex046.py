"""
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
    mostre os 10 primeiros termos dessa progressão.
"""
print("=" * 30)
print(f"10 termos de uma PA".upper())
print("=" * 30)
primeiro = int(input("Primeiro termo:"))
razao = int(input("Razão: "))
#tratamento dos 10 termos
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print(f"{i} ->", end=" ")
print("FIM")