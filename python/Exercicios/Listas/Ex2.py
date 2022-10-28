#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for x in range(10):
    num = int(input('Digite o numero:'))
    lista.append(num)

lista.reverse()
print(lista)