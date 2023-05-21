"""
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa, mostre: a média de idade do grupo,
    qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
mulheres = 0
media = 0
maioridadehomem = 0
velho = ''
for i in range(1, 5):
    print(f"=== {i}ª PESSSOA ===")
    nome = str(input("Nome:")).title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [H/M]: ")).lower()
    #tratamento media do grupo
    media = media + idade
    #tratamento mulheres menor que 20
    if sexo == "m" and idade < 20:
        mulheres += 1
    #tratamento homem mais velho
    if i == 1 and sexo == "h":
        maioridadehomem = idade
        velho = nome
    if sexo == "h" and idade > maioridadehomem:
        maioridadehomem = idade
        velho = nome

print(f"A media de idade do grupo é {media / 4:.0f} anos")
print(f"O homem mais velho tem {maioridadehomem} e se chama {velho}")
print(f"{mulheres} mulheres tem menos de 20 anos")