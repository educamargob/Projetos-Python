from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.http import HttpResponse
from cadastro_clientes.models import Cliente
from .forms import *

def index(request):
    return render(request, 'index.html')

def cadastro_clientes(request):
    form = ClientesForms()
    contexto = {'form':form}
    return render(request, 'clientes/cadastro_clientes.html', contexto)

def cria_cliente(request):
    """Inserir cliente no sistema"""
    if request.method == 'POST':
        nome_cliente = request.POST['nome_cliente']
        endereco = request.POST['endereco']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        cep = request.POST['cep']
        cnpj = request.POST['cnpj']
        cliente = Cliente.objects.create(nome_cliente=nome_cliente, endereco=endereco, bairro=bairro, cidade=cidade, cep=cep, cnpj=cnpj)
        cliente.save()
        return redirect('index')

def mostra_cliente(request):
    if request.method == 'POST':
        form = ClientesForms(request.POST)
        contexto = {'form':form}
        return render(request, 'clientes/mostra_cliente.html', contexto)