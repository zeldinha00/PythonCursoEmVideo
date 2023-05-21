### Desafio 01 - Faça um programa que leia duas notas de um aluno e mostre a media entre elas.

name = str(input("Digite seu nome: ")).title()
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"{name}, a média entre {nota1} e {nota2} é igual a {media:.2f}.\n")

