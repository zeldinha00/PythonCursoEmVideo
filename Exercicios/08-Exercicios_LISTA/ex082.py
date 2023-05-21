"""
    Crie um programa que declare uma matriz de dimensão 3×3
    e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação corret

    Aprimore o desafio, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
"""

matriz = []

# Preenchendo a matriz com os valores fornecidos pelo usuário
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a matriz na tela
print("Matriz:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print()

# Somando os valores pares
soma_pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            soma_pares += valor

# Somando os valores da terceira coluna
soma_terceira_coluna = 0
for linha in matriz:
    soma_terceira_coluna += linha[2]

# Encontrando o maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print("Soma dos valores pares:", soma_pares)
print("Soma dos valores da terceira coluna:", soma_terceira_coluna)
print("Maior valor da segunda linha:", maior_segunda_linha)