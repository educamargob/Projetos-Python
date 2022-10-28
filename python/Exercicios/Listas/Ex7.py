#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import math
numeros = []

for x in range(5):
    num = int(input(f'Digite o {x+1}° numero:'))
    numeros.append(num)

produto = math.prod(numeros)

print(f'Soma {sum(numeros)}')
print(f'Multiplicação {produto}')