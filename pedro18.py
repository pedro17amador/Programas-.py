from random import choice
print('Um professor esta escolhendo um dos alunos para limpar a lousa...')
a = input('Digite um nome: ')
b = input('Digite outro nome: ')
c = input('Digite outro nome: ')
d = input('Digite mais um nome: ')
aluno = choice([a, b, c, d])
print('O(a) aluno(a) sortiado(a) é: {}'.format(aluno))
