# Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
l = float(input('Seja bem vindo ao Vítor Tintas, descubra aqui quanto você precisa de tinta para pintar sua parede.\nQual é a largura de sua parede em METROS?'))
h = float(input('E qual é a altura de sua parede em METROS?'))
a = l*h
t = a/2
print ('A área de sua parede é de {:.2f} metros quadrados, logo, para pinta-lá você gastará {:.2f} Litros de tinta'.format(a,t))