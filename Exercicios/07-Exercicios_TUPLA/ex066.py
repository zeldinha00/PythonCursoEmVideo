"""
    Tuplas são imutáveis
    Tuplas () lista [] dicionario {}
    sorted = ordem alfabetica ou numerica
    .count = conta quantos itens está na tupla
    .index = posição do item na tupla

    Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
    de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
extenso = ("zero", "um", "Dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")

while True:
    numero = int(input("Digite um numero de 0 a 10: "))
    if 0 <= numero <= 20:
        break
    print("TENTE NOVAMENTE", end=" ")
print(f"O numero digitado foi {extenso[numero]}")