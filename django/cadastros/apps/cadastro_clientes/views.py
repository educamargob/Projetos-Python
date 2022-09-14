from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.http import HttpResponse
from cadastro_clientes.models import Cliente, Estados
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *

@login_required
@staff_member_required
def lista_clientes(request):
    """Listar os clientes cadastrados"""
    clientes = Cliente.objects.order_by('-data_criacao')
    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    clientes_por_pagina = paginator.get_page(page)
    dados = {
        'clientes' : clientes_por_pagina
    }
    return render(request, 'clientes/listar_clientes.html', dados)

@login_required
@staff_member_required
def cadastro_clientes(request):
    """Cadastro de clientes"""
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
    else:
        form = ClientesForms()
        contexto = {'form':form}
        return render(request, 'clientes/cadastro_clientes.html', contexto)

@login_required  
@staff_member_required
def deleta_cliente(cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')

@login_required  
@staff_member_required
def altera_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = ClientesForms(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClientesForms(instance=cliente)
    cliente_editar = { 'form':form }
    return render(request, 'clientes/edita_cliente.html', cliente_editar)

