"""
    # Desafio 002
    - Faça um programa que leia o nome de uma pessoa e mostre uma menssagem de boas-vindas.

    DICA: Na aula de hoje eu quero te mostrar como funciona a função input no Python!
    Essa é uma função que permite com que você solicite uma informação ao usuário para que ele possa preencher,
    seja para responder uma pergunta, seja para fazer o login em um sistema.
    Vou te mostrar os cuidados com input no Python, pois por padrão as informações solicitadas são registradas
    no formato de texto (string), por esse motivo, temos que tomar cuidado ao registrar um número,
    data ou qualquer outra informação.

"""

#   Exemplo01
name = input("Digite seu nome: ").title()
print(f"É um prazer te conhecer, {name}")

#   Exemplo02 .format
sub_name = input("Digite seu nome sobrenome: ").title()
print("Seu nome completo é '{} {}'!!!".format(name, sub_name))
