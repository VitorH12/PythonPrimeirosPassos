frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:22])
print(frase[1:15:2])
print(frase[::2])
''' print("""Para avançar no andamento dos cursos você precisa sempre:
1) Ver o vídeo até o final
2) Clicar no botão de "CLIQUE AQUI PARA MARCAR COMO CONCLUÍDO" das aulas, capitulos, módulos e cursos após ver o vídeo ou antes de avançar para aula seguinte.
Assistindo ao vídeo até o final e clicando no botão de concluído ele deve conseguir avançar sem problemas.""") #NOVA FUNÇÃO AI '''
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python','Do Vitão'))
print(frase) #string é imutável, replace não altera a frase, apenas substitui no comando ali
print(frase.find('Curso'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[0][2])