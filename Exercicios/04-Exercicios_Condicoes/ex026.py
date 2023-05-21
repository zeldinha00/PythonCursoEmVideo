#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um numero: "))
resultado = numero % 2

if resultado == 0:
    print(f"Numero digitado foi {numero} é PAR!!!")
else:
    print(f"Numero digitado foi {numero} é IMPAR!!!")