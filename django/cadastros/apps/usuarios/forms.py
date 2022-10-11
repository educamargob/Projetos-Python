from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from usuarios.validation import *
from datetime import datetime
from usuarios.models import Mensagens

class cadastroMensagemForms(forms.ModelForm):
    data_criacao = forms.DateField(label='Data da criação', disabled=True, initial=datetime.today)
    class Meta:
        model = Mensagens
        fields = '__all__'
        labels = {'icon':'Icone'}
        
class loginClienteForms(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput())
    senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())

class cadastroClienteForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='Email', max_length=100, widget=forms.EmailInput())
    senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())
    senha2 = forms.CharField(label='Confirmação de senha', max_length=100, widget=forms.PasswordInput())

    def clean(self):
        nome = self.cleaned_data.get('nome')
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')
        lista_de_erros = {}
        valida_senha(senha, senha2, 'senha2', lista_de_erros)
        valida_username(nome, 'nome', lista_de_erros)
        valida_email(email, 'email', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data



