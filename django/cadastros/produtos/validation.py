def campo_ntem_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numerico"""
    if any(not char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua letras nesse campo'

def verifica_imagem(valor_campo, nome_campo, lista_de_erros):
    """Verifica se foi inserido imagem"""
    if valor_campo is None:
        lista_de_erros[nome_campo] = 'Favor inserir uma imagem'
