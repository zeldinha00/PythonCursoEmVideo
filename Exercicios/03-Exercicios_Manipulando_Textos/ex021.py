# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome da cidade: ")).strip().title()
print(f"Começa com Santos: {cidade[0:5] == 'Santo'}")  #modelo 1 -  ver apenas o inicio de 0 a 5


# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Digite seu nome: ")).strip().title()
print(f"Seu nome tem Silva: {'Silva' in nome}")  #modelo 2 - percorre toda string para ver se tem a palavra Santos

