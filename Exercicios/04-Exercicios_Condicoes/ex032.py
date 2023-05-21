"""
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
    o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

cores = {
    'limpa': '\033[m',
    'amarelo': '\033[4:33m',
    'verde': '\033[0:32m',
    'vermelho': '\033[0:31m'
}

valor_casa = float(input("Qual o valor da casa: R$ "))
salario = float(input("Qual o valor do salário: R$ "))
tempo = int(input("Quanto vai ter o financiamento: "))

prestacao = valor_casa / (tempo * 12)
minimo = salario * 30 / 100

print(f"Para pagar a casa de R$ {valor_casa:.2f} em {tempo} a prestação sera de R$ {prestacao:.2f}")
if prestacao <= minimo:
    print(f"Emprestimo {cores['verde']}CONCEDIDO{cores['limpa']}")
else:
    print(f"Emprestimo {cores['vermelho']}NEGADO{cores['limpa']}")
