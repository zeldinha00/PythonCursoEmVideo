"""
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
parenteseEsquerda = []
parenteseDireita = []
exp = str(input("Digite sua expreção: "))
for i in exp:
    if i == "(":
        parenteseEsquerda.append(i)
    elif i == ")":
        parenteseDireita.append(i)
if len(parenteseEsquerda) == len(parenteseDireita):
    print("Sua expressão está CERTA!!!")
else:
    print("Sua expressão está INCORRETA!!!")



