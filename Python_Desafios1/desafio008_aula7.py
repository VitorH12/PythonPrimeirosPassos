# Escreve um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite um valor em metros:'))
cm = m*100
mm = m*1000
print ('{}m convertido para centímetros equivale a {:.1f}cm e em milímetros equivale a {:.1f}mm'.format(m,cm,mm))