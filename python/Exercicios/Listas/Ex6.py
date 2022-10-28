#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
alunos_notas = []
alunos_medias = []
cont = 0
for x in range(3):
    notas = []
    for nota in range(2):     
        nota = float(input(f'Digite a {nota+1}° do {x+1}° aluno: '))
        notas.append(nota)
    alunos_notas.append(notas)

print(alunos_notas)

for notas in alunos_notas:
    media = sum(notas) / len(notas)
    alunos_medias.append(media)

print(alunos_medias)

for media in alunos_medias:
    if media >= 7.0:
        cont += 1

print(f'Existem {cont} alunos com a média acima de 7')
        