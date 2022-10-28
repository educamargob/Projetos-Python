#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
caracteres = []
consoantes = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
cont = 0
consoantes_lidas = []
for x in range(10):
    car = input(f'Digite o {x+1} caractere:')
    caracteres.append(car)

for caractere in caracteres:
    if caractere.lower() in consoantes:
        cont += 1
        consoantes_lidas.append(caractere)

print(f'Foram lidas {cont} consoantes {consoantes_lidas}')