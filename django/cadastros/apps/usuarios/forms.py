from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from usuarios.validation import *
from datetime import datetime

class loginClienteForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    senha = forms.CharField(label='Email', max_length=100, widget=forms.PasswordInput())

class cadastroClienteForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())
    senha2 = forms.CharField(label='Confirmação de senha', max_length=100, widget=forms.PasswordInput())

    def clean(self):
        lista_de_erros = {}
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data



