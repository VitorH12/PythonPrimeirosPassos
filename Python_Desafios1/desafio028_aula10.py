'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o uuário tentar descobrir, mostrando se ele acertou ou não.'''
import random
from time import sleep #firula pra aparecer um carregando
escolha = random.randint(0,5)
print("Vou pensar em um número entra 0 e 5, Tenta adivinhar...")
chute = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(2)
if escolha == chute:
    print("ACERTOU")
else:
    print("GANHEI, Pensei em {} e você chutou {}".format(escolha,chute))