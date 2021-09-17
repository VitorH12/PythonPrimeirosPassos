'''Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7 por Km acima do limite.'''
velocidade = float(input("Qual é a velocidade do seu carro? "))
if velocidade > 80.0:
    multa = (velocidade-80)*7.0
    print("MULTADO -> Valor: R${:.2f}".format(multa))
else:
    print("Tenha um ótimo dia")