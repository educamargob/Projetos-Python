"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a.Mostre a quantidade de valores que foram lidos;
b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d.Calcule e mostre a soma dos valores;
e.Calcule e mostre a média dos valores;
f.Calcule e mostre a quantidade de valores acima da média calculada;
g.Calcule e mostre a quantidade de valores abaixo de sete;
h.Encerre o programa com uma mensagem;"""

def imprimir_notas(notas):
    for nota in notas:
        print(nota, end=' ')
    print()

def imprimir_notas_inverso(notas):
    notas.reverse()
    for nota in notas:
        print(nota)
    
def somar_notas(notas):
    soma = sum(notas)
    return soma

def media_notas(notas):
    media = sum(notas) / len(notas)
    return media

def acima_da_media(notas, media):
    cont = 0
    for nota in notas:
        if nota > media:
            cont += 1
    return cont

def abaixo_de_sete(notas):
    cont = 0
    for nota in notas:
        if nota < 7:
            cont += 1
    return cont

inserir = True
notas = []
notas_reverse = []
media = 0
while inserir:
    nota = float(input(f'Digite a {len(notas)+1}° nota: '))
    if nota != -1:
        notas.append(nota)
    else:
        inserir = False
        print('SISTEMA ENCERRADO')

print(f'Valores lidos {len(notas)}')

imprimir_notas(notas)
imprimir_notas_inverso(notas)
soma = somar_notas(notas)
media = media_notas(notas)
acima_media = acima_da_media(notas, media)
abaixo_sete = abaixo_de_sete(notas)


print(f'Soma das notas : {soma}')
print(f'Média das notas : {media}')
print(f'Notas acima da média : {acima_media}')
print(f'Notas abaixo de 7 : {abaixo_sete}')



