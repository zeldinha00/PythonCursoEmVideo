"""
    ### Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
     que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input("Qual a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você está acima do limite 80km/h e sua multa é de R$ {multa:.2f}")
else:
    print("Você está na velocidade permitida")
