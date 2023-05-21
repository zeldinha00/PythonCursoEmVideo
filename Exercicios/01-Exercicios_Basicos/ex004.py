"""
    -~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

  + -> Adição              ** -> Potencia
  - -> Subtração           // -> Divisão inteira
  * -> Multiplicação        % -> Resto da divisão
  / > Divisão -


           Ordem de Precedência

  1° -> ()
  2° -> **
  3° -> *  /  //  %
  4° -> +  -

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

nome = int(input("Digite seu nome do programa: "))
print("{:^20}".format(nome).upper())       #centraliza o texto
print("{:=^20}".format(nome).upper())      #adiciona caracteres e centraliza o texto
print("{:>20}".format(nome).upper())       #jogo o texto para direita
print("{:<20}".format(nome).upper())       #jogo o texto para Esquerda
print("{:.2f}".format(nome).upper())    #casas depois da virgula

"""

### Desafio 01 - Faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor

num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
print(f"O número digitado foi {num}, seu sucessor é {suc} e seu antecessor é {ant}.\n")

### Simplificando o codigo

num = int(input("Digite um número: "))
print(f"O número digitado foi {num}, seu sucessor é {num+1} e seu antecessor é {num-1}")







