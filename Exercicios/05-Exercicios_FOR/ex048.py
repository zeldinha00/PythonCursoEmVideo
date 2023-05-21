"""
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
    Exemplos de palíndromos:
    APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
frase = str(input("Digite a frase: ")).strip().upper()
# tratamento em lista
palavras = frase.split()
# tratamento em uma strig
junto = ''.join(palavras)
# tratamento inverso da string
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"O inverso de  {junto} é {inverso}")
# solucao do problema
if inverso == junto:
    print("Temos um Palíndromo")
else:
    print("Não é um Palíndromo")
