# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos km você percorreu com esse carro durante {:.0f} dia(as)?'.format(d)))
custod = d*60
custokm = km*0.15
custo = custod + custokm
print('O custo total por ter usado o carro durante {:.0f} dia(as) e percorrido com ele por {:.2f}Km é de R${:.2f}'.format(d,km,custo))