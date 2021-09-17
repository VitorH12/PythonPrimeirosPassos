'''Crie um programa que leia uma frase pelo teclado e mostre:
'Quantas vezes aparece a letra 'A'
Em que posição ela aparece a priemira vez e em que posição ela aparece pela última vez'''
frase = str(input("Digite uma frase: ")).strip()
fraseM = frase.upper()

quantidade = fraseM.count('A')
ondePrimeiraVez = fraseM.find('A')+1
ondeUltimaVez = fraseM.rfind('A')+1
#caracteres = len(frase)
#fraseinvertida = (frase[::-1])
#ondeUltimaVez = caracteres-fraseinvertida.find('A')
print('Quantidade de vezes: {}\nPrimeira vez: {}\nÚltima vez: {}'.format(quantidade,ondePrimeiraVez,ondeUltimaVez))
