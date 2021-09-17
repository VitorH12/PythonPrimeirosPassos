'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex: digite um número: 1834'''
'Unidade:4 Dezena:3 Centena:8 Milhar:1'
num = int(input("Informe um número: "))

uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
milha = num // 1000 % 10

print("Unidade: ",uni,"\nDezena: ",dez,"\nCentena: ",cent,"\nMilhar: ",milha)
