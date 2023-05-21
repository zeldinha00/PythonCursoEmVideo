def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print(f"\033[1;31mValor inválido. Digite um número inteiro válido.\033[m")


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[36m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[32mSua Opção: \033[m")
    return opc



