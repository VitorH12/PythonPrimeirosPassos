'''Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza -> primeiro: Ana -> último: Souza'''
nome = str(input("Digite um nome: ")).strip()
lista = nome.split()
primeiroNome = lista[0]
ultimoNome = (lista[len(lista)-1])
print("Primeiro nome: {}\nÚltimo nome: {}".format(primeiroNome,ultimoNome))

'''
lista = nome.split( )
quantidadeCaracteres = len(primeironome)
ultimaCaracter - primeironome[len(primeironome)-']
quantidadeVezesLista = len(lista)
ultimonome = lista[quantidadeVezesLista-1]'''