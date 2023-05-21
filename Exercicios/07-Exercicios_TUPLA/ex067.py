"""
    Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
    do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time da Goias.
"""

times = (
"Botafogo",
"Palmeiras",
"Cruzeiro",
"Fortaleza",
"São Paulo",
"Fluminense",
"Grêmio",
"Internacional",
"Bahia",
"Athletico-PR",
"Vasco",
"Bragantino",
"Cuiabá",
"Santos",
"Atlético-MG",
"Flamengo",
"Corinthians",
"Goiás",
"Coritiba",
"América-MG",
)
print("=-" * 30)
print(f"Lista dos times do Brasileirão: {times}")
print("=-" * 30)
print(f"Lista dos times dos 5 primeiros colocados: {times[0:5]}")
print("=-" * 30)
print(f"Lista dos times dos 4 ultimos colocacados: {times[-4:]}")
print("=-" * 30)
print(f"Lista dos times em ordem alfabetica: {sorted(times)}")
print("=-" * 30)
print(f"O Goias está na {times.index('Goiás') + 1}")



