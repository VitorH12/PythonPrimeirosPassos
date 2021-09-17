# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
p = str(input('Digite o nome de um aluno(a):'))
s = str(input('Digite o nome de um outro aluno(a):'))
t = str(input('Digite o nome de mais um aluno(a):'))
q = str(input('Digite pela última vez o nome de mais um aluno(a):'))
list = [p, s, t, q] #lista em python é em [ ]
random.shuffle(list)
print('A ordem de apresentação é:',list)