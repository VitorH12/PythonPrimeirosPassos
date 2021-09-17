'''Desenvolva um programa que leia o comprimento de 3 retas e diga se forma um triangulo'''
r1 = float(input("Digita o comprimento da reta a: "))
r2 = float(input("Digita o comprimento da reta b: "))
r3 = float(input("Digita o comprimento da reta c: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("FORMA TRIANGULO")
else:
    print("NÃO FORMA UM TRIANGULO")