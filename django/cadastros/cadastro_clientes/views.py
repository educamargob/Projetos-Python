from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.http import HttpResponse
from cadastro_clientes.models import Cliente, Estados
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

def index(request):
    return render(request, 'index.html')

def lista_clientes(request):
    clientes = Cliente.objects.order_by('-data_criacao')
    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    clientes_por_pagina = paginator.get_page(page)
    dados = {
        'clientes' : clientes_por_pagina
    }
    return render(request, 'clientes/listar_clientes.html', dados)

def cadastro_clientes(request):
    form = ClientesForms()
    contexto = {'form':form}
    return render(request, 'clientes/cadastro_clientes.html', contexto)

def cria_cliente(request):
    """Inserir cliente no sistema"""
    if request.method == 'POST':
        form = ClientesForms(request.POST)
        if form.is_valid():
            nome_cliente = request.POST['nome_cliente']
            endereco = request.POST['endereco']
            bairro = request.POST['bairro']
            cidade = request.POST['cidade']
            estado = request.POST['estado']
            cep = request.POST['cep']
            cnpj = request.POST['cnpj']
            cliente = Cliente.objects.create(nome_cliente=nome_cliente, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, cep=cep, cnpj=cnpj)
            cliente.save()
            return redirect('lista_clientes')
        else:
            contexto = {'form':form}
            return render(request, 'clientes/cadastro_clientes.html', contexto)
            
def mostra_cliente(request):
    if request.method == 'POST':
        form = ClientesForms(request.POST)
        contexto = {'form':form}
        return render(request, 'clientes/mostra_cliente.html', contexto)


