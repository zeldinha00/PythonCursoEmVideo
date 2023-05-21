from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'listaCadastrada.txt'

if not aquivoExiste(arquivo):
    criarAquivo(arquivo)

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar pessoa', 'Sair do sistemas'])
    if resposta == 1:
        # Opção de listar o contéudo de um aquivo!
        lerAquivo(arquivo)
    elif resposta == 2:
        # Opção de cadastrar uma pessoa!
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema!
        cabecalho("Saindo do sistemas...Até Logo!")
        break
    else:
        # Opção errada!
        print("\033[1;31mERROR: Digite uma opção válida!\033[m")
    sleep(1)