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
enquete = [1500,3500,3000,500,150,150]
while inserir:
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print("1 - Windows Server")
    print("2 - Unix")
    print("3 - Linux")
    print("4 - Netware")
    print("5 - Mac OS")
    print("6 - Outro")
    voto = int(input())
    if voto == 0:
        inserir = False
        break
    contabiliza_voto(voto, enquete)

soma_votos = sum(enquete)

print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')
print(f'Windows Server           {enquete[0]}   17%')
print(f'Unix                     {enquete[1]}   17%')
print(f'Linux                    {enquete[2]}   17%')
print(f'Netware                  {enquete[3]}   17%')
print(f'Mac OS                   {enquete[4]}   17%')
print(f'Outro                    {enquete[5]:<2}   17%')
print('-------------------     -----')
print(f'Total                    {soma_votos}')
#print(f'O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {} dos votos.')