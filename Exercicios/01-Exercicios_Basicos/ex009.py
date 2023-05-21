# Faça um programa que leia um valor que você tem na carteira e mostra qtos dolar vc pode comprar
# Considere o que o dolar é US$ 1.00 = R$ 3.27

real = float(input("Digite o valor que você tem em reais na carteira: R$ "))
dolar = real / 3.27

print(f"Você tem na carteira R$ {real:.2f} e pode comprar USD {dolar:.2f}")
