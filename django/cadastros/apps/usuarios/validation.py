from django.contrib.auth.models import User

def valida_senha(valor_senha, valor_senha2, nome_campo, lista_de_erros):
    """Verifica se as senhas correspondem"""
    if(valor_senha != valor_senha2):
        lista_de_erros[nome_campo] = 'As senhas não correspondem'

def valida_username(valor_nome, nome_campo, lista_de_erros):
    """Verifica se nome de usuário ja é utilizado"""
    if User.objects.filter(username=valor_nome).exists():
        lista_de_erros[nome_campo] = 'Nome de usuário já utilizado'

def valida_email(valor_email, nome_campo, lista_de_erros):
    """Verifica se email ja é utilizado"""
    if User.objects.filter(email=valor_email).exists():
        lista_de_erros[nome_campo] = 'Endereço de Email já utilizado'