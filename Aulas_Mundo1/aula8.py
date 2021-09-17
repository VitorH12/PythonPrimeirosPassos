import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num) #repare que quando coloca math. aparece TODAS as importações
raizold = num**(1/2)
print ('A old raiz de {} é {} e a new raiz de {} é {}'.format(num,raizold,num,raiz))
print ('Agora arredondando para cima a raiz de {} é {} e arredondando para baixo é {}'.format(num,math.ceil(raiz),math.floor(raiz)))
