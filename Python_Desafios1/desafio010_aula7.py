# Crie um programa que leia quanto dinheiro uma pessoa tem na carteire e mostre quantos Dólares ela pode comprar (Considere 1$=R$3,27)
r = float(input('Qual o valor em reais você tem disponível para comprar dollar: R$'))
d = r/3.27
print ('Com R${} você pode comprar aproximadamente U${:.2f}'.format(r,d))