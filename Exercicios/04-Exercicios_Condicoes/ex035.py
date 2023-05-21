"""
     Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
     vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
     Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime

#informando o sexo
sexo = int(input("""Informe seu sexo:
[ 1 ] Masculino
[ 2 ] Feminino
Opção: """))

#tratando sexo
if sexo == 1:
    print("Prossiga para a proxima etepa")
else:
    print("Sexo Feminino não deve alistar")
    quit()

#pegando a data atual
ano_atual = datetime.datetime.now().year
#pegando a data de nascimento
nascimento = int(input("Informe sua data de nascimento: "))
#Convertendo nascimento por idade atual.
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.")

#Tratamento menor de idade
if idade < 18:
    tempo = 18 - idade
    print(f"Falta para você se alistar {tempo} anos")
    alistamento = ano_atual + tempo
    print(f"Seu alistamento sera em {alistamento}")
#Tratamento maior de idade
elif idade > 18:
    tempo = idade - 18
    print(f"Você já deveria ter se alistado há {tempo} anos")
    alistamento = ano_atual - tempo
    print(f"Você deveria se alistar em {alistamento}")
#Tratamento 18 anos
else:
    print(f"Você tem que se alistar IMEDIATAMENTE")
