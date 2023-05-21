"""
    Melhore o DESAFIO EX056, perguntando para o usuário se ele quer mostrar mais alguns termos.
    O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

primeiro = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} > ", end=" ")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print(f"FIM, foi mostrado um total de {total} termos")

