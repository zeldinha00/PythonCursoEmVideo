"""
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep

def maior(* num):
    cont = maior = 0
    print("-=" * 30)
    print("Analisando os valores passados...")
    for valor in num:
        print(f"{valor} ", end="")
        sleep(0.3)
        # tratamento MAIOR menor
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}")


# Programa Principal
maior(5, 6, 6, 4, 5)
maior(4, 7, 8,)
maior(1, 2)
maior()
