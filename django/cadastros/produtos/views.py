from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.http import HttpResponse
from produtos.models import Produtos, Categorias
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

def index(request):
    """Mostrar a página principal para o usuário com sistema de paginas"""
    produtos = Produtos.objects.order_by('-data_criacao')
    paginator = Paginator(produtos, 3)
    page = request.GET.get('page')
    produtos_por_pagina = paginator.get_page(page)

    dados = {
        'produtos' : produtos_por_pagina
    }

    return render(request, 'index.html', dados)

def lista_produtos(request):
    produtos = Produtos.objects.order_by('-data_criacao')
    paginator = Paginator(produtos, 10)
    page = request.GET.get('page')
    produtos_por_pagina = paginator.get_page(page)
    dados = {
        'produtos' : produtos_por_pagina
    }
    return render(request, 'produtos/listar_produtos.html', dados)

def cadastro_produtos(request):
    form = ProdutosForms()
    contexto = {'form':form}
    return render(request, 'produtos/cadastro_produtos.html', contexto)

def cria_produto(request):
    """Inserir produto no sistema"""
    if request.method == 'POST':
        form = ProdutosForms(request.POST, request.FILES)
        if form.is_valid():
            nome_produto = request.POST['nome_produto']
            categoria = request.POST['categoria']
            preco = request.POST['preco']
            descricao = request.POST['descricao']
            foto_produto = request.FILES['foto_produto']
            produto = Produtos.objects.create(nome_produto=nome_produto, categoria=categoria, preco=preco, descricao=descricao, foto_produto=foto_produto)
            produto.save()
            return redirect('lista_produtos')
        else:
            contexto = {'form':form}
            return render(request, 'produtos/cadastro_produtos.html', contexto)
            
def mostra_produto(request):
    if request.method == 'POST':
        form = ProdutosForms(request.POST)
        contexto = {'form':form}
        return render(request, 'produtos/mostra_produto.html', contexto)


