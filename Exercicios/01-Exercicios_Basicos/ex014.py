"""
    ### Faça um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade
    de dias pelo qual foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
    e R$0,15 por km rodado.
"""
dias = int(input("Quantos dias alugados: "))
km = float(input("Quantos km rodados: "))
total = (dias * 60) + (km * 0.15)
print(f"O total a pagar é de R$ {total:.2f}")
