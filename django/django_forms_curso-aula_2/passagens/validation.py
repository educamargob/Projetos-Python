def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino sao iguais"""
    if origem == destino:
            lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numerico"""
    if any(char.isdigit() for char in valor_campo):
            lista_de_erros[nome_campo] = 'Não inclua números nesse campo'
