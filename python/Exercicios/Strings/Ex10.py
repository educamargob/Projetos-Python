"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
"""
num_extenso = {0 : 'zero',
        1 : 'um',
        2 : 'dois',
        3 : 'três',
        4 : 'quatro',
        5 : 'cinco',
        6 : 'seis',
        7 : 'sete',
        8 : 'oito',
        9 : 'nove',
        10 : 'dez',
        11 : 'onze',
        12 : 'doze',
        13 : 'treze',
        14 : 'quatorze ou catorze',
        15 : 'quinze',
        16 : 'dezesseis',
        17 : 'dezessete',
        18 : 'dezoito',
        19 : 'dezenove',
        20 : 'vinte',
        30 : 'trinta',
        40 : 'quarenta',
        50 : 'cinquenta',
        60 : 'sessenta',
        70 : 'setenta',
        80 : 'oitenta',
        90 : 'noventa'
}
def num_por_extenso(numero):
    if numero > 20 and numero not in num_extenso:
        unidade = numero % 10
        num = (numero - unidade)
        msg = (f"O numero {numero} por extenso é {num_extenso[num].upper()} E {num_extenso[unidade].upper()}")
    else:
        msg = (f"O numero {numero} por extenso é {num_extenso[numero].upper()}")
    return msg

while True:
    numero = int(input('Digite um numero entre 0 e 99: '))
    if(numero >= 0 and numero <= 99):
        break
    else:
        print("Tente novamente! ", end="")


print(num_por_extenso(numero))
