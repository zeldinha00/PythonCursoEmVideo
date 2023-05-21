"""
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('Roger', 'carro', 'cidade', 'bola', 'banana', 'caneta', 'esacola', 'martelo', 'panela', 'norte')

for p in palavras:
    print(f"\nNa palavra \033[32m{p.upper()}\033[0;0m temos ", end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f"\033[33m{letra}\033[0;0m", end=' ')
