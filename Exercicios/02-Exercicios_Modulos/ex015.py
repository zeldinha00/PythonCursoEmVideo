"""
     math -> Biblioteca de operadores aritméticos {

     sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
     floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
     ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
     hypot() ---> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
     pow() ----> Potencia de um numero ---------------- pow(2, 3) = 2³ = 8
     radians()-> Converte em graus radianos ---------- print(math.radians(180))
     cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
     sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
     tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))
  }

    ### Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porçao inteira:
    EX: ditite o numero 6.127 tem a parte inteira 6
"""
### Biblioteca matematica importada
import math

num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua porção é {math.floor(num)}")
