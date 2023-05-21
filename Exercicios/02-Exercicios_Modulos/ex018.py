"""
      random -> Gerar numeros pseudoaleatorios {

      randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
      choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
      shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)
  }

    ### Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa
    que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

    DICA: biblioteca random
"""
import random
aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno:"))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choices(alunos)
print(f"O aluno escolhido foi {escolhido}.")
random.shuffle(alunos)
print(f"Sequencia aleatoria {alunos}")