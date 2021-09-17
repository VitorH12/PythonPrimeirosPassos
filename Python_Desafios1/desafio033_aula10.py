'''Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor'''
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
if a > b and a > c:
        maior = a
if b > c and b > a:
        maior = b
if c > a and c > b:
        maior = c
print("Maior: {}\nMenor: {}".format(maior,menor))