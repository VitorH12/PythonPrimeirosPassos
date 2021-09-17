from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num) #NOTE QUE IMPORTANDO APENAS SQRT E FLOOR, NÃO É NECESSÁRIO COLOCAR .math antes
print ('A raiz de {} arredondando para baixo é {}'.format(num,floor(raiz)))
