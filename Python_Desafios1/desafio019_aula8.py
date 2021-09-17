# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome delas e escrevendo o nome do escolhido.
from random import choice
p = str(input('Digite o nome do primeiro aluno(a):'))
s = str(input('Digite o nome do segundo aluno(a):'))
t = str(input('Digite o nome do terceiro aluno(a):'))
q = str(input('Digite o nome do quarto aluno(a):'))
r = choice([p,s,t,q])
print ('O aluno(a) sorteado(a) para apagar o quadro é {}'.format(r))