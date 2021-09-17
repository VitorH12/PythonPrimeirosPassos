# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número para saber o seu dobro, triplo e sua raiz quadrada:'))
d = n*2
t = n*3
r = n**(1/2)
print ('Segue o dobro, o triplo e a raiz quadrada de {}:\n dobro: {};\n triplo: {};\n raiz quadrada: {:.2f} . '.format(n,d,t,r))
#o :.0f é pra ficar sem nenhuma casa depois da vírgula