'''Crie um programa que leia o nome completo de uma pessoa e mostre:
 -O nome com todas as letras maiúsculas;
 -O nome com todas as letras minúsculas
 -Quantas letras ao todo tem o nome (sem considerar os espaços)
 -Quantas letras tem o primeiro nome'''
nome = str(input("Digite seu nome completo: ")).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
quantidadeLetras = len(nome)-nome.count(' ')
lista = nome.split()
quantidadePrimeiro = len(lista[0])
#quantidadePrimeiro = nome.find(' ')

print("Maiúsculo: ",maiusculo)
print("Minúsculo: ",minusculo)
print("Quantidade de letras: ",quantidadeLetras)
print("Quantidade de letras 1° nome: ",quantidadePrimeiro)