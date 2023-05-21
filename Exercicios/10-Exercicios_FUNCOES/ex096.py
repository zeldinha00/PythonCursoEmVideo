"""
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
    o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
    OPCIONAL e OBRIGATÓRIO nas eleições.
"""
def voto(ano):
    # tratamendo idade atual
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    # tratamento votos
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


# Programa Principal
ano = int(input("Ano de nascimento: "))
print(voto(ano))




