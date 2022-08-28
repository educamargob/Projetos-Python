def campo_ntem_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numerico"""
    if any(not char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua letras nesse campo'
