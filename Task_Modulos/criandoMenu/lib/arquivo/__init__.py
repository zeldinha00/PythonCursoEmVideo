from Task_Modulos.criandoMenu.lib.interface import *


def aquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do aquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso")


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("ERRO ao ler o arquivo")
    else:
        cabecalho('PESSOAS CADASTRADA(s)')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(aquivo, nome='Desconhecido', idade=0):
    try:
        a = open(aquivo, 'at+')
    except:
        print("Ouve um erro na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Ouve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado")
            a.close()













