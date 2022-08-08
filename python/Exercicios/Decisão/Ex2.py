def apresentacao():
    b1 = float(input("Nota Bimestre 1: "))
    b2 = float(input("Nota Bimestre 2: "))
    media = calcula_media(b1, b2)
    verifica_aprovacao(media)

def calcula_media(b1, b2):
    media = (b1 + b2)/2
    return media

def verifica_aprovacao(media):
    if media == 10:
        print(f"Aluno aprovado com Distinção com media {media}")
    elif media >= 7:
        print(f"Aluno aprovado com media {media}")
    else:
        print(f"Aluno reprovado com média {media}")

if __name__ == "__main__":
    apresentacao()