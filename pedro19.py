
from random import shuffle
print("O professor vai sortear os alunos para a ordem de apresentação do seminário")
a = input('Primeiro aluno:')
b = input('Segundo aluno:')
c = input('Terceiro aluno:')
d = input('Quarto aluno:')
aluno = [a, b, c, d]
shuffle(aluno)
print('A ordem dos alunos sorteados será {}'.format(aluno))
