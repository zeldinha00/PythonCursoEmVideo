"""
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
    mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
resposta = "S".upper()
soma = media = quantidade = maior = menor = 0
while resposta in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = (str(input("Deseja continuar [S / N]: "))).upper().strip()[0]
media = soma / quantidade
print(f"ACABOU, Você digitou {quantidade} numeros e a media entre eles é {media:.2f}")
print(f"O maior digitado foi {maior} e o menor foi {menor}")
