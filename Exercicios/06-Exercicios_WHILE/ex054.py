"""
    Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.
"""
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
menu = 0

while menu != 5:
    menu = int(input("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\n
Escolha uma opção:  """))

    if menu == 1:
        total = num1 + num2
        print(f"A soma de {num1} + {num2} = {total}")
    elif menu == 2:
        total = num1 * num2
        print(f"A multiplicação de {num1} x {num2} = {total}")
    elif menu == 3:
        if num1 > num2:
            print(f"{num1} maior que {num2}")
        elif num1 == num2:
            print(f"{num1} mesmo valor que {num2}")
        else:
            print(f"{num2} maior que {num1}")
    elif menu == 4:
        print("Informe os novos valores>>>")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif menu == 5:
        print("Fim do programa")
        quit()
    else:
        print("Opção invalida, digite um numero valido!!!")
    print("=-" * 20)