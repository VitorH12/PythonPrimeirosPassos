#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit e Kelvin.
c = float(input('Informe uma temperatura em °C:'))
f = c * 1.8 + 32
k = c + 273
print('{}°C equivale a {:.2f}°F e a {:.2f}K .'.format(c,f,k))