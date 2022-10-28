#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = []
par = []
impar = []
for x in range(5):
    num = int(input(f'Digite o {x+1}° numero:'))
    numeros.append(num)

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'Lista de numeros {numeros}\nNumeros pares {par}\nNumeros impares{impar}')