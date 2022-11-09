"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u.
"""
vogais = ['a','e','i','o','u']
frase = input('Frase: ')
cont_vogais = 0;
cont_espacos = 0;
for caractere in frase:
    if caractere.lower() in vogais:
        cont_vogais += 1
    if caractere == ' ':
        cont_espacos += 1

print(f"A frase contem {cont_vogais} vogais e {cont_espacos} espaços em branco")