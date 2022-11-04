"""
    Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações
    Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
"""
def contabiliza_voto(voto, enquete):
    if voto == 1:
        enquete[0] += 1
    elif voto == 2:
        enquete[1] += 1
    elif voto == 3:
        enquete[2] += 1
    elif voto == 4:
        enquete[3] += 1
    elif voto == 5:
        enquete[4] += 1
    elif voto == 6:
        enquete[5] += 1
    else:
        print('SELEÇÃO INCORRETA')


inserir = True
#enquete = [1500,3500,3000,500,150,150]
enquete = []
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
for sistema in sistemas:
    enquete.append(0)
while inserir:
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    for sistema in sistemas:
        print(f"{sistemas.index(sistema)+1} - {sistema}")
    voto = int(input())
    if voto == 0:
        inserir = False
        break
    contabiliza_voto(voto, enquete)

soma_votos = sum(enquete)

if sum(enquete) != 0:
    maior = 0
    sis = ""
    per = 0
    print('Sistema Operacional     Votos    %')
    print('-------------------     -----   ----')
    for sistema in sistemas:
        porcentagem = round(enquete[sistemas.index(sistema)] / sum(enquete) * 100)
        print(f"{sistema:<24}{enquete[sistemas.index(sistema)]:>5}{porcentagem:>6}%")
        if maior < enquete[sistemas.index(sistema)]:
            maior = enquete[sistemas.index(sistema)]
            sis = sistema
            per = porcentagem

    print('-------------------     -----')
    print(f'Total{soma_votos:>24}')
    print(f'O Sistema Operacional mais votado foi o {sis}, com {maior} votos, correspondendo a {per}% dos votos.')
else:
    print("A enquete não possui votos...")