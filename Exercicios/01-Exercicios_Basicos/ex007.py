### Desafio 04 - Faça um programa que leia valor em metros e exiba convertidos em centimentros e milimetros.

metros = int(input("Informe os metros: "))
centimentros = metros * 100
milimetros = metros * 1000
print(f"Metros informados foi {metros} em centimentros é {centimentros:.0f}cm e em milimetros é {milimetros:.0f}mm\n")

#Reduzindo o codigo
n = float(input('Uma distancia em metros:'))
print(f'A medida de {n}m corresponde a\n{n/1000}km\n{n/100}hm\n{n/10}dam\n{n}m\n{n*10}dm\n{n*100}cm\n{n*1000}mm')