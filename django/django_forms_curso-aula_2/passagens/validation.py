def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino sao iguais"""
    if origem == destino:
            lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numerico"""
    if any(char.isdigit() for char in valor_campo):
            lista_de_erros[nome_campo] = 'Não inclua números nesse campo'

def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se data de ida é maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser maior que data de ida'

def data_ida_menor_data_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se a data de ida é menor que a data de hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor hoje'

