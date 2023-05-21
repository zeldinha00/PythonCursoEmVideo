"""
    Tuplas ()
    Listas []
    Dicionarios {}

    ESTUDOS
"""
estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
print(brasil)

for c in brasil:
    for e in c.values():
        print(e, end=" ")
    print()
