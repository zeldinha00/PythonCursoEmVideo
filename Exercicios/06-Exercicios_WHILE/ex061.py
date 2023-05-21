"""
    Faça um programa que mostre a tabuada de vários números, um de cada vez,
    para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
numero = 0
while True:
        numero = int(input("Quer ver a tabuada de qual valor: "))
        if numero < 0:
            break
        print("=" * 15)
        for c in range (1, 11):
           print(f"{c} x {numero} = {c*numero}")
        print("=" * 15)
print("Fim")
