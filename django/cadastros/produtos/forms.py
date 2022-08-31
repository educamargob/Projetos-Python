from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from produtos.validation import *
from datetime import datetime
from produtos.models import Produtos, Categorias

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ProdutosForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProdutosForms, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['class'] = 'mask-preco'
    data_criacao = forms.DateField(label='Data da criação', disabled=True, initial=datetime.today)
    class Media:
        js= (
            "js/form.js",
        )
    class Meta:
        model = Produtos
        fields = '__all__'
        labels = {'nome_produto':'Nome'}


    def clean(self):
        preco = self.cleaned_data.get('preco')
        lista_de_erros = {}
        campo_ntem_numero(preco, 'preco', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data