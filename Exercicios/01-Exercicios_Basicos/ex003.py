"""
 -~-~-~-~-~-~-~-~- Tipos primitivos ~-~-~-~-~-~-~-~-~-

  int()  --> Para números inteiros ------------ 17, 21, 35, 42

  float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1

  bool() --> Armazena True ou False --------True, False

  str() ----> Conjunto de caracteres -------- 'narigudo', 'Pedro', 'feioso'

  type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    ### Desafio: Crie um programa que leia dois numeros e mostre a soma deles:

    ### Desafio: Crie um programa que leia algo e der alguns detalhes sobre ele:

"""

#Exemplo 01

n1 = input("Digite um numero: ")
n2 = input("Digite outro numero: ")
soma = n1 + n2
print(f"Não ouve soma pois são uma string: {soma} do tipo", type(soma))

#Desafio 01

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print(f"A soma dos número {n1} e {n2}  é: {soma} do tipo", type(soma))

#Desafio 02

algo = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(algo))
print("Só tem espaços? ", algo.isspace())
print("Só tem números? ", algo.isnumeric())
print("Só tem alfabético? ", algo.isalpha())
print("Está em maiúculas?", algo.isupper())
print("Esá em minúsculas? ", algo.islower())