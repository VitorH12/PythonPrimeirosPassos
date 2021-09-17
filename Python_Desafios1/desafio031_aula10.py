'''Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por km para viagem de ate 200Km e 0,45 para viagens mais longas'''
distancia = float(input("Qual a distância da sua viagem em Km? "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preço é R${:.2f}".format(preco))