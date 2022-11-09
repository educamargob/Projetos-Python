"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO

"""
nome = input('Digite seu nome: ')
cont = 1
for char in nome:
    for ca in range(cont):
        print(nome[ca].upper(),end='')
    cont += 1
    print()