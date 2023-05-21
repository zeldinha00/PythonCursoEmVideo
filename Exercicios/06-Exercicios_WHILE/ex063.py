"""
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
    o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.
"""
print("=" * 25)
print("SITEMAS CADASTRAMENTO")
print("=" * 25)
pessoas = maiores = homens = mulheres20 = 0
while True:
    idade = int(input("Idade: "))
    tipo = ' '
    while tipo not in "MF":
        tipo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    pessoas += 1
    if idade >= 18:
        maiores += 1
    if tipo == 'M':
        homens += 1
    if idade >= 20 and tipo == "F":
        mulheres20 += 1
    new = ' '
    while new not in "SN":
        new = str(input("Quer continuar: [S/N]: ")).upper().strip()[0]
    if new == "N":
        break
print(f"""TOTAL CADASTRADO: {pessoas}
TOTAL MAIORES DE 18 ANOS: {maiores}
TOTAL DE HOMENS CADASTADO: {homens}
TOTAL MULHERES MAIORES DE 20 ANOS: {mulheres20}
""")
