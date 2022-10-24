arquivo_contatos = open('dados/contatos-escrita.csv', mode='a+', encoding='latin_1')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n'
            '13,Tais,tais@tais.com.br\n'
            '14,Felipe,felipe@felipe.com.br\n'
            ]

for contato in contatos:
    arquivo_contatos.write(contato)

#Força a inserção dos dados dentro do arquivo
arquivo_contatos.flush()
#Fecha o arquivo e salva
#arquivo_contatos.close()

#Busca pelo numero do caractere
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha, end='')
