'''Faça um programa que leia um ano qualquer e mostre se ela é bissexto'''
from datetime import date #pra saber o dia de hoje
ano = int(input("Digite um ano e coloque 0 caso seja o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano é BISSEXTO")
else:
    print("Não é BISSEXTO")