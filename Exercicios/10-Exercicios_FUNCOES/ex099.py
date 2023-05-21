"""
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
    só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print(f"\033[1;31mValor inválido. Digite um número inteiro válido.\033[m")

n = leiaInt('Digite um número inteiro: ')
print("Você digitou:", n)