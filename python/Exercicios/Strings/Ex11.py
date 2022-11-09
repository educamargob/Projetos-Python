"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
import random
palavras = []
palavra_dicas = []
def carrega_palavras(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo_usuarios:
        for linha in arquivo_usuarios:
            linha = linha.rstrip('\n')
            palavras.append(linha.split(' - '))
    for i in palavras:
        for j in i:
            if i.index(j) == 0:
                palavra = j
            else:
                dica = j
        palavra_dicas.append({"palavra":palavra,"dica":dica})
    print(palavra_dicas)

def jogo_forca():
    carrega_palavras('arquivos/palavras_forca.txt')
    random.shuffle(palavra_dicas)
    palavra = palavra_dicas[0]["palavra"]
    dica = palavra_dicas[0]["dica"]
    palavra = palavra.upper()
    letras_chute = []
    letras_erro = []
    print("-------JOGO DA FORCA-------", end="\n\n")
    print(f"Dica: {dica}")
    mostra_acertos(palavra, letras_chute)
    chutar(palavra, letras_chute, letras_erro)
    

def chutar(palavra, lista_chutes, lista_erros):
    chutes = 5
    erros = 0
    acertos = 0
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    while chutes > 0:
        chute = input("Digite uma letra: ")
        chute = chute.upper()
        lista_chutes.append(chute)
        if len(chute) == 1 and chute not in numeros:
            if chute in palavra:
                acertos += 1
                mostra_acertos(palavra, lista_chutes)
            else:
                lista_erros.append(chute)
                chutes -= 1
                erros += 1 
                if chutes != 0:
                    print(f"Você errou pela {erros}ª vez, {chutes} chutes restantes. Tente de novo!\n")  
                    mostra_acertos(palavra, lista_chutes)      
                else:
                    print(f"Você errou pela {erros}ª vez!") 
                    print("-------FIM DE JOGO-------")
            if acertos == len(palavra):
                chutes = 0
                print(f"\nPARABÉNS VOCÊ GANHOU") 
                print("-------FIM DE JOGO-------")
        else:
            print("Por favor digite UMA letra")

def mostra_acertos(palavra, chutes):
    for letra in palavra:
                if letra in chutes:
                    print(letra, end=" ")
                else:
                    print("_", end=" ")
    

jogo_forca()