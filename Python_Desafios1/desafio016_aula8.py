# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Número 6,
# 85849494 -> parte inteira: 6
import math
n = float(input('Computador diga um número qualquer:'))
print ('A porção inteira de {} é {}'.format(n,math.floor(n))) #trunc -> deixa o número inteiro tbm