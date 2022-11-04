"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""
import os
def byte_para_megabyte(valor):
    megabyte = valor / 1024 / 1024
    return megabyte

def arquivo_linhas(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo_usuarios:
        for linha in arquivo_usuarios:
            usuarios.append(linha.split())
            
usuarios = []
espaco_utilizado = []
arquivo_linhas('arquivos/usuarios.txt')

os.remove('arquivos/relatorio.txt')
arquivo_relatorio = open('arquivos/relatorio.txt', mode='a+', encoding="utf-8")
arquivo_relatorio.truncate(0)

arquivo_relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n\n')
for usuario in usuarios:
    for dado in usuario:
        if usuario.index(dado) == 1:
            mega = byte_para_megabyte(float(dado))
            espaco_utilizado.append(mega)
for usuario in usuarios:
    for dado in usuario:
        if usuario.index(dado) == 1:
            mega = byte_para_megabyte(float(dado))
    arquivo_relatorio.write(f'{usuarios.index(usuario)+1:<5}{usuario[0]:<15}{round(mega,2):>7} MB{round(mega/sum(espaco_utilizado)*100, 2):>17} %\n')
arquivo_relatorio.write(f'\nEspaço total ocupado: {round(sum(espaco_utilizado),2)} MB\nEspaço médio ocupado: {round(sum(espaco_utilizado)/len(espaco_utilizado),2)} MB')

arquivo_relatorio.close()
            