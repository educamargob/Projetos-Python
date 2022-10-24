import contatos_utils
try:
    # contatos = contatos_utils.csv_para_contatos('dados/contatos.csv')
    # contatos_utils.contatos_para_pickle(contatos, 'dados/contatos.pickle')

    # contatos = contatos_utils.pickle_para_contatos('dados/contatos.pickle')
    # contatos_utils.contatos_para_json(contatos, 'dados/contatos.json')

    contatos = contatos_utils.json_para_contatos('dados/contatos.json')
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
    # with open('dados/contatos.csv', encoding='latin_1') as arquivo_contatos:
    #     for linha in arquivo_contatos:
    #         print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem Permissão de escrita')