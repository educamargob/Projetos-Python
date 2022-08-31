from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from cadastro_clientes.validation import *
from datetime import datetime
from cadastro_clientes.models import Cliente, Estados

class ClientesForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientesForms, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
        self.fields['cnpj'].widget.attrs['class'] = 'mask-cnpj'
        
    data_criacao = forms.DateField(label='Data da criação', disabled=True, initial=datetime.today)
    class Media:
        js= (
            "js/form.js",
        )
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {'nome_cliente':'Nome','endereco':'Endereço','cnpj':'CNPJ','cep':'CEP'}



    def clean(self):
        nome_cliente = self.cleaned_data.get('nome_cliente')
        bairro = self.cleaned_data.get('bairro')
        cidade = self.cleaned_data.get('cidade')
        lista_de_erros = {}
        campo_tem_numero(nome_cliente, 'nome_cliente', lista_de_erros)
        campo_tem_numero(bairro, 'bairro', lista_de_erros)
        campo_tem_numero(cidade, 'cidade', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data