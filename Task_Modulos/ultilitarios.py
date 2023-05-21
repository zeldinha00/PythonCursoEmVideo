def aumentado(price=0, taxa=0, formato=False):
    """
    ==> Função usada para aumentar a porcentagem (%) do valor a ser executado
    :param price: valor a ser usado na função
    :param taxa: taxa a ser executada em relação ao price
    :param formato: formatar os price das dos valores reais
    :return: retornar a execução da função
    """
    resp = price + (price * (10 / 100))
    return resp if formato is False else moeda(resp)


def diminuir(price=0, taxa=0, formato=False):
    """
    ==> Função usada para diminuir a porcentagem (%) do valor a ser executado
    :param price: valor a ser usado na função
    :param taxa: taxa a ser executada em relação ao price
    :param formato: formatar os price das dos valores reais
    :return: retornar a execução da função
    """
    resp = price - (price * (10 / 100))
    return resp if formato is False else moeda(resp)


def dobro(price=0, formato=False):
    """
    ==> Função usada para dobrar o valor do price
    :param price: valor a ser usado na função
    :param formato: formatar os price das dos valores reais
    :return: retornar a execução da função
    """
    resp = price * 2
    return resp if formato is False else moeda(resp)


def metade(price=0, formato=False):
    """
    ==> Função usada para dividi o valor do price na metade
    :param price: valor a ser usado na função
    :param formato: formatar os price das dos valores reais
    :return: retornar a execução da função
    """
    resp = price / 2
    return resp if formato is False else moeda(resp)


def moeda(price=0, moeda='R$'):
    """
    ==> Função usada para formatar os valores reais (R$) '.' para ','
    :param price: valor a ser formatado
    :param moeda: forma a moeda
    :return: retorna a função
    """
    return f'{moeda}{price:.2f}'.replace('.', ',')


def resumo(price=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(price)}')
    print(f"O Dobro do preço: \t{dobro(price, True)}")
    print(f"O Dobro do preço: \t{dobro(price, True)}")
    print(f"O Metade do preço: \t{metade(price, True)}")
    print(f"Com {taxaa}% aumento: \t{aumentado(price, taxaa, True)} ")
    print('-' * 30)



