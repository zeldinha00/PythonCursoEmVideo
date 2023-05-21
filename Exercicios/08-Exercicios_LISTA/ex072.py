"""
    LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores
    em uma mesma estrutura, acessíveis por chaves individuais.
    tuplas = ()  imutáveis ou seja não pode ser alterada
    lista = []  composta pode ser alterada
        .append adiciona no final da lista
        .insert(0 , item) vai adiciona um novo elemento no inicio da lista
        .pop(indice do alemento a ser deletado) se for apenas .pop deleta o ultimo elemento
        .remove('nome do elemento a ser deletado')
        del lanche[2]
        .sort() organiza os elementos .sort(reverse = True) ordem crescente de traz para frente

        TREINO OS COMANDOS <<<<<
"""

numeros = [1, 10, 5, 83, 9, 4]
print(numeros)
numeros[2] = 3 #troca o elemento indicado pelo indice
print(numeros)
numeros.sort()#organiza do maior para o menor
print(numeros)
numeros.sort(reverse=True) #faz o inverso da lista maior para menor
print(numeros)
numeros.append(99) #adiciona um novo elemento no final da lista
print(numeros)
numeros.pop()
print(numeros) #remove o ultimo elemento da lista
numeros.pop(0)
print(numeros) #remove o indice indicado no pop
numeros.remove(4)  #remove o elemento que estiver dentro da lista
print(numeros)
print(f"Esta lista tem {len(numeros)} elementos na lista") # ver o tamanho da lista