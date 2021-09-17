# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Digite sua primeira nota de Matemática 1:'))
n2 = float(input('Digite sua segunda nota de Matemática 1:'))
s = int(input('Valor da prova:'))
mnotas = (n1+n2)/2
mprova = s*0.6
mtotal = mnotas>=mprova
print ('-> LEGENDA <- True: Alcançou a média, False: Não Alcançou a média;\n A média de suas notas foi de:{:.1f}\n Você alcançou a média da prova:{}'.format(mnotas,mtotal))
