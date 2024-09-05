import random
alunos = []
c = 0
while True:
  aluno = str(input('Vamos descobrir quem é o aluno sorteado. (digite 0 para parar o sorteio). Digite o nome da pessoa: '))
  if aluno == '0':
    break
  else:
    alunos.append(aluno) # Adiciona o aluno à lista
    sorteio = alunos[random.randint(0, len(alunos)-1)] # Escolhe um aluno aleatório
    print(sorteio, 'é o sorteado!!')
    break # Para o loop depois de selecionar um aluno
