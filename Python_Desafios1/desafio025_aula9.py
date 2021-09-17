'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome'''
nome = str(input("Digite o seu nome: ")).strip()
nomeM = nome.upper()
silva = "SILVA" in nomeM
print("Seu nome contém 'Silva'? ",silva)