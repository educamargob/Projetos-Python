from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from cadastro_clientes.estados import estados
from cadastro_clientes.validation import campo_tem_numero

class ClientesForms(forms.Form):
    nome_cliente = forms.CharField(label='Nome', max_length=100)
    endereco = forms.CharField(label='Endereço', max_length=100)
    bairro = forms.CharField(label='Bairro', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    estado = forms.ChoiceField(label='Estado', choices=estados)
    cep = forms.CharField(label='CEP', max_length=8)
    cnpj = forms.CharField(label='CNPJ', max_length=14)

    def clean(self):
        nome_cliente = self.cleaned_data.get('nome_cliente')
        bairro = self.cleaned_data.get('bairro')
        cidade = self.cleaned_data.get('cidade')
        lista_de_erros = {}
        campo_tem_numero(nome_cliente, 'nome_cliente', lista_de_erros)
        campo_tem_numero(bairro, 'bairro', lista_de_erros)
        campo_tem_numero(cidade, 'cidade', lista_de_erros)