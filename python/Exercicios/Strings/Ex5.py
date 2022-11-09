"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

"""

nome = input('Digite seu nome: ')
cont = len(nome)
for char in nome:
    for ca in range(cont):
        print(nome[ca].upper(),end='')
    cont -= 1
    print()