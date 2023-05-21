"""
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
    o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se
    será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(n, show=False):
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end=" ")
            if cont > 1:
                print(" x ", end=" ")
            else:
                print(" = ", end=" ")
        f *= cont
    return f


# Programa Principal
print(fatorial(5))
