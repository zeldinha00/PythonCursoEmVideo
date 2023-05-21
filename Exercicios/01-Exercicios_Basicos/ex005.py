### Desafio 01 - Faça um programa que leia o seu dobro, seu triplo e sua raiz quadrada.

num1 = int(input("Digite um número: "))
dobro = num1 * 2
triplo = num1 * 3
raiz = num1**(1/2)
print(f"""O dobro de {num1} é {dobro}.
O triplo de {num1} é {triplo}.
A raiz quadrada de {num1} é {raiz:.2f}.\n""")

## Reduzindo o codigo

print(f"""O dobro de {num1} é {num1*2}.
O triplo de {num1} é {num1*3}.
A raiz quadrada de {num1} é {num1**(1/2):.2f}.\n""")
