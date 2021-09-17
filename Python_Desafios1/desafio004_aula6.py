# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
n1 = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(n1))
print('"', n1, '" é um número?', n1.isnumeric())
print(n1, 'é um número ou uma palavra?', n1.isalnum())
print(n1, 'é uma palavra?', n1.isalpha())
print(n1, 'é um número decimal?', n1.isdecimal())
print(n1, 'é um espaço', n1.isspace())
