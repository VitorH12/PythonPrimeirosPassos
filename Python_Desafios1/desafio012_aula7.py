# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
v = float(input('Digite o valor de um produto que você queira na loja:R$'))
d = v*0.95
print('Parabéns, comprando com nós hoje, você paga R${:.2f}'.format(d))