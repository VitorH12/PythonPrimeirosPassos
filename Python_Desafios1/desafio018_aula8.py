# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
x = float(input('Digite um ângulo e descubra seu seno, cosseno e tangente:'))
y = radians(x)
s = sin(y)
c = cos(y)
t = tan(y)
print ('* O seno é:{:.4f};\n* O cosseno é:{:.4f};\n* E a tangente é:{:.4f}'.format(s,c,t))