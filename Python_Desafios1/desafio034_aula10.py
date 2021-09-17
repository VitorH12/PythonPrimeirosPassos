'''Pergunte salario de funcionario. se for superior a 1250 calcule aumento de 10%, inferiores ou iguais, aumento de 15%'''
salario = float(input("Qual é o seu salário? R$"))
if salario <= 1250.0:
    novo = salario*1.15
else:
    novo = salario*1.10
print("Novo salário: RS{:.2f}".format(novo))
