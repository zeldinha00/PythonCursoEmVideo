"""
    Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
    a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
num = int(input("Digite um numero: "))
(print("""Escolha uma das bases para conversão
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL"""))
escolha = int(input("Escolha sua opção: "))

if escolha == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif escolha == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif escolha == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção invalida, tente novamente.")