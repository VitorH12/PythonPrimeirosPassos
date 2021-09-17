# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
x = float(input('Digite o cateto oposto de um triângulo retângulo:'))
y = float(input('Digite o cateto adjacente desse mesmo triângulo:'))
hip = hypot(x,y)
print('A hipotenusa é {:.2f}'.format(hip))
