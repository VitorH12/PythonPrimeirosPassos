import random, emoji #importei uma biblioteca de emoji
num = random.randint(1,25) #computador vai dizer um número aleatório de 1 a 25
print(emoji.emojize('{} Olá mundo :earth_americas:'.format(num), use_aliases=True,))