"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

palindromo = input("Digite uma frase: ")

palindromo = palindromo.replace(" ", "")
palindromo_reverso = palindromo[::-1]
print(palindromo)
print(palindromo_reverso)

if(palindromo == palindromo_reverso):
    print("A frase é um palindromo")
else:
    print("A frase não é palindromo")