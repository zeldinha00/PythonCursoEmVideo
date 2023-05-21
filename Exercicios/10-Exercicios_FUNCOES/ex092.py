"""
     Faça um programa que tenha uma função chamada escreva(),
     que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
     Ex:
     escreva(‘Olá, Mundo!’) Saída:
     ~~~~~~~~~
     Olá, Mundo!
     ~~~~~~~~~
"""
def escreva(titulo):
    tamanho = len(titulo) + 4
    print("=" * tamanho)
    print(f"  {titulo}")
    print("=" * tamanho)

escreva("CADASTRAMENTO DE PESSOAS")