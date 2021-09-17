'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra Santo'''
cid = str(input("Digite uma cidade: ")).strip()
cidM = cid.upper()
comecaSanto = (cidM[:5] == "SANTO")
print("Começa com Santo? ",comecaSanto)
