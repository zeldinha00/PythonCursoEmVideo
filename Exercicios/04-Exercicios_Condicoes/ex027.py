"""
    ### Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
        cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
distancia = float(input("Qual a distância da sua viagem: "))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f"Sua viagem vai ter {distancia}km e o valor da passagem é R${valor:.2f}")
