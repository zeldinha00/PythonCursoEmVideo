"""
     Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
     de acordo com a média atingida:

    – Média abaixo de 5.0: REPROVADO
    – Média entre 5.0 e 6.9: RECUPERAÇÃO
    – Média 7.0 ou superior: APROVADO
"""
nota1 = float(input("Insira o valor da primeira prova: "))
nota2 = float(input("Insira o valor da segunda prova:  "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2}, a média do aluno é {media}")
if media < 5:
    print(f"Média abaixo de 5.0: REPROVADO")
elif 5 < media < 7:
    print("Média entre 5.0 e 6.9: RECUPERAÇÃO")
else:
    print("Média 7.0 ou superior: APROVADO")