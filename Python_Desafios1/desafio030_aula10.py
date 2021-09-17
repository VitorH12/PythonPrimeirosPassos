'''Crie um programa que leia um número inteiro e diga se é par ou impar'''
num = int(input("Digite um número: "))
resultado = num % 2
if resultado == 0:
    print("PAR")
else:
    print("ÍMPAR")