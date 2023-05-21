"""
    Crie um módulo chamado ultilitarios.py que tenha as funções incorporadas
                  aumentar(),diminuir(),dobro()metade().
    Faça também um programa que importe esse módulo e use algumas dessas funções.

    Adapte o código, criando uma função adicional chamada
    moeda() que consiga mostrar os números como um valor monetário formatado

    Modifique as funções que foram criadas para que elas aceitem um parâmetro a mais,
    informando se o valor retornado por elas vai ser ou não formatado pela função moeda().

    Adicione o módulo ultilitarios.py criado nos desafios anteriores, uma função chamada resumo(),
    que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

"""
import ultilitarios

num = float(input("Digite o preço: R$ "))
ultilitarios.resumo(num)




