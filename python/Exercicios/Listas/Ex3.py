#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for x in range(4):
    nota = int(input(f'Digite a {x+1}° nota :'))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"As notas do aluno são: {notas} e a média ficou {media}")