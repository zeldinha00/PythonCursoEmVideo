"""
    # Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
      separadamente.
"""
nome = str(input("Digite seu nome completo: ")).strip().title()
print("Muito prazer em te conhecer!")
lista = nome.split()
print(f"Seu primeiro nome é {lista[0]}")
print(f"Seu ultimo nome é {lista[len(lista)-1]}")
