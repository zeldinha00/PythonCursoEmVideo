def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: retornoa o valor do fatorial de um número n.
    """
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