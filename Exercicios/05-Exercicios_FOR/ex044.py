"""
    Refaça o DESAFIO 'ex008', mostrando a tabuada de um número que o usuário escolher,
    só que agora utilizando um laço for.
"""
num = int(input("Digite um numero para ver sua tabuada: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
