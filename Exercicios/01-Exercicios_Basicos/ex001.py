"""
    Desafio 001
    - Crie um programa que escreva "Olá, Mundo!" na tela.

    A função print() é uma das funções mais importantes e usadas na linguagem Python.
    Sua função é, basicamente, exibir mensagens na tela ou enviá-las para outro dispositivo,
    como imprimir dentro de arquivos de texto.

    No Python 3, print() é uma função interna, de modo que não é necessário importar
    nenhuma biblioteca para poder utilizá-la. Basta chamá-la e passar os argumentos necessários.

    No Python 2, print era uma declaração, o que significa que não era possível realizar determinadas ações
    como atribuir o retorno de sua chamada a uma variável ou outra declaração, por exemplo.

    DICA: OBS: Um ponto importante a considerar é que a função print() converte implicitamente
    todos os argumentos para string, chamando a função str() (conversão de tipos para string),
    e assim consegue tratar a saída de dados como string de modo uniforme.
"""

# Exemplo 01

for c in range(0, 5):
    print(c)

print("Olá, Mundo!")

# Exemplo 02 Concatenação de Strings

name = input("Digite seu nome: ")
print("Olá " + name + "!. Bem-vindo ao curso de Python!\n")

# Exemplo 03 Concatenação de Strings
print(f"Olá {name}!. Bem-vindo ao curso de Python!\n")

# Exemplo 04 Concatenação de Strings
print("Olá {}!. Bem-vindo ao curso de Python!\n".format(name))




