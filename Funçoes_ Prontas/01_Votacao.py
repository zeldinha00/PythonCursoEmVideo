def voto(ano):
    """
    ==> Simples sistemas de validação de voto, para saber se a idade a pessoa VOTA,OPCIONAL,OBRIGATORIO
    :param ano: Ano de nascimento para tratamento idade atual
    :return: retorna resolução em relação a votação.
    """
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
    