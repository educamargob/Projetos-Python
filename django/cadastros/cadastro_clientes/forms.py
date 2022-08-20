from django import forms

class ClientesForms(forms.Form):
    nome_cliente = forms.CharField(label='Nome', max_length=100)
    endereco = forms.CharField(label='Endereço', max_length=100)
    bairro = forms.CharField(label='Bairro', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    cep = forms.CharField(label='CEP', max_length=8)
    cnpj = forms.CharField(label='CNPJ', max_length=14)