"""          s  t  f
        \033[1:30:41m    conteudo    \033[m    cores no terminal 01 stilo - 02 cor texto - 03 cor do fundo
          style     texto           fundo
          0 none    30  branco      40 branco
          1 bold    31  vermelho    41 vermelho
          4 undline 32  verde       42 verde
          7 negat   33  amarelo     43 amarelo
                    34  azul        44 azul
                    35  roxo        45 roxo
                    36  oceano      46 oceano
                    37  cinza       47 cinza

         Refaça o DESAFIO 31 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

        – EQUILÁTERO: todos os lados iguais
        – ISÓSCELES: dois lados iguais, um diferente
        – ESCALENO: todos os lados diferentes

"""
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.



cores = {
    'limpa':'\033[m',
    'amarelo':'\033[4:33m',
    'verde':'\033[0:32m',
    'vermelho':'\033[0:31m'
}



print("-=-" * 10)
print(f"{cores['amarelo']}Analisando triangulo{cores['limpa']}")
print("-=-" * 10)

lado1 = float(input("Primeiro segmento: "))
lado2 = float(input("Seungdo segmento: "))
lado3 = float(input("Terceiro segmento: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print(f"{cores['verde']}SIM, podem formar um Tiangulo.{cores['limpa']}")
    if lado1 == lado2 == lado3:
        print(f"Triangulo {cores['verde']}EQUILÁTERO{cores['limpa']}")
    elif lado1 != lado2 != lado3 != lado1:
        print(f"Triangulo {cores['verde']}EESCALENO{cores['limpa']}")
    else:
        print(f"Triangulo {cores['verde']}ISÓCELES{cores['limpa']}")

else:
    print(f"{cores['vermelho']}NÃO, podem formar um Triangulo.{cores['limpa']}")


