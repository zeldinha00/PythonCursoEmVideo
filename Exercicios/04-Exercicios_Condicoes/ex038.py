"""
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
    e mostre seu status, de acordo com a tabela abaixo:

    – IMC abaixo de 18,5: Abaixo do Peso
    – Entre 18,5 e 25: Peso Ideal
    – 25 até 30: Sobrepeso
    – 30 até 40: Obesidade
    – Acima de 40: Obesidade Mórbida

    DICA: MC = peso / altura²
"""
peso = float(input("Informe seu peso: (kg) "))
altura = float(input("Informe sua altura: (m) "))
#calculo do IMC
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} - ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f} - PESO IDEAL")
elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f} - SOBREPESO")
elif 30 <= imc < 40:
    print(f"Seu IMC é {imc:.2f} - OBESIDADE")
else:
    print(f"Seu IMC é {imc:.2f} - OBESIDADE MÓRBIDA")
