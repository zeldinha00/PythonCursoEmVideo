# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

ano = int(input("Que ano quer analisar? digite 0 para o ano atual: "))

if ano == 0:  #pegar o ano atual
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é BISSEXTO.")