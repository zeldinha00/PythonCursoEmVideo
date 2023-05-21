"""
     Elabore um programa que calcule o valor a ser pago por um produto, considerando
     o seu preço normal e condição de pagamento:

    – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço formal
    – 3x ou mais no cartão: 20% de juros
"""

print(f'{" LOJA ZELDINHA ":=^40}')
compras = float(input("Preço das compras: R$"))
forma_compras = int(input("""FORMA DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção: """))

if forma_compras == 1:
    desconto = compras - (compras * 10 / 100)
    print(f"Sua compra de R$ {compras:.2f} vai custar R$ {desconto:.2f} no final.")
elif forma_compras == 2:
    desconto = compras - (compras * 5 / 100)
    print(f"Sua compra de R$ {compras:.2f} vai custar R$ {desconto:.2f} no final.")
elif forma_compras == 3:
    desconto = compras / 2
    print(f"Sua compra de R$ {compras:.2f} fica parcelado em 2x de R$ {desconto:.2f} sem juros.")
elif forma_compras == 4:
    parcelas = int(input("quantas parcelas: "))
    if parcelas >= 3:
        parcelamentos = (compras / parcelas)
        juros = parcelamentos + (parcelamentos * 20 / 100)
        total_parcelado = juros * parcelas
        print(f"Sua compra sera parcelado em {parcelas}x de R${juros:.2f} com JUROS")
        print(f"Sua compra que era de {compras} vai ficar R$ {total_parcelado:.2f} ")
    else:
        print("Parcelas tem que ser em 3x ou mais...")
        quit()
else:
    print("Opção invalida!!! digite um opção valida.")
    quit()
print("Obrigado pelas compras, volte sempre!!!")
