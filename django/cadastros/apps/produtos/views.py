from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from produtos.models import Produtos, Categorias
from django.core.paginator import Paginator
from .forms import *

def index(request):
    """Mostrar a página principal para o usuário com sistema de paginas"""
    produtos = Produtos.objects.order_by('-data_criacao')
    paginator = Paginator(produtos, 6)
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
            form.save()
            return redirect('lista_produtos')
        else:
            contexto = { 'form':form }
            return render(request, 'produtos/cadastro_produtos.html', contexto)

def deleta_produto(request, produto_id):
    """Deletar um produto do sistema"""
    produto = Produtos.objects.get(id=produto_id)
    produto.delete()
    return redirect('lista_produtos')

def altera_produto(request, produto_id):
    """Alterar dados de um produto"""
    produto = Produtos.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutosForms(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutosForms(instance=produto)
    produto_editar = { 'form':form }
    return render(request, 'produtos/edita_produto.html', produto_editar)

def produto(request, produto_id):
    produto = Produtos.objects.get(id=produto_id)
    dados = {
        'produto':produto
    }
    return render(request, 'produtos/produto.html', dados)



