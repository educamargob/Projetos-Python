import time
from django.shortcuts import render
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from webpush import send_user_notification
from usuarios.models import Mensagens
from firebase_admin.messaging import Message, Notification
from firebase_admin.messaging import Message
from fcm_django.models import FCMDevice


def cadastro_notificacao(request):
    """Realiza o cadastro de push-notifications ou mostra a tela de cadastro"""
    if request.method == 'POST':
        form = cadastroMensagemForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastro_usuario')
        else:
            form = cadastroMensagemForms(request.POST, request.FILES)
            contexto = {
                'form':form
            }
            return render(request, 'usuarios/login.html', contexto)
    else:
        form = cadastroMensagemForms()
        contexto = {
            'form' : form
        }
        return render(request, 'notificacoes/cadastro_notificacoes.html', contexto)


def teste2(request):
    device = FCMDevice.objects.all().first()
    device.send_message(Message(
        notification=Notification(title="title", body="text", image="url"),
        topic="Optional topic parameter: Whatever you want",
    ))
def teste(request):
    mensagens = Mensagens.objects.order_by('-data_criacao').filter(habilitada=True)
    x = 0
    while x == 0:
        for mensagem in mensagens:
            icone = ''
            if mensagem.icon:
                icone = mensagem.icon.url
            else:
                icone = 'https://universo.adami.com.br/static/user/assets/images/logo_universo.png'

            payload = {"head": mensagem.titulo, "body": mensagem.corpo_mensagem,
                        "icon": icone, "url": "http://127.0.0.1:8000/"}    
            print(payload)
            usuario = User.objects.get(id=1)
            send_user_notification(user=usuario, payload=payload, ttl=1000)
            time.sleep(15)
            x = 0
    return render(request, 'index.html')
    

def cadastro_usuario(request):
    """Realiza o cadastro de usuários ou mostra a tela de cadastro"""
    if request.method == 'POST':
        form = cadastroClienteForms(request.POST)
        if form.is_valid():
            nome = request.POST['nome']
            email = request.POST['email']
            senha = request.POST['senha']
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login_usuario')
        else:
            form = loginClienteForms()
            form2 = cadastroClienteForms(request.POST)
            contexto = {
                'form_login':form,
                'form_cadastro':form2
            }
            return render(request, 'usuarios/login.html', contexto)
    else:
        return redirect('login_usuario')

def login_usuario(request):
    """Realiza o login de um usuário no sistema"""
    if request.method == "POST":
        form = loginClienteForms(request.POST)
        if form.is_valid():
            email = request.POST['email']
            senha = request.POST['senha']
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    return redirect('index')
    else:
        form = loginClienteForms()
        form2 = cadastroClienteForms()
        contexto = {
            'form_login':form,
            'form_cadastro':form2
        }
        return render(request, 'usuarios/login.html', contexto)

def logout_usuario(request):
    """Realiza o logout no sistema"""
    auth.logout(request)
    return redirect('index')

@login_required
@staff_member_required
def lista_usuarios(request):
    """Mostrar usuários cadastrados no sistema"""
    usuarios = User.objects.order_by('-date_joined')
    paginator = Paginator(usuarios, 50)
    page = request.GET.get('page')
    usuarios_por_pagina = paginator.get_page(page)
    dados = {
        'usuarios' : usuarios_por_pagina
    }
    return render(request, 'usuarios/lista_usuarios.html', dados)

@login_required
@staff_member_required
def altera_usuario(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = cadastroClienteForms(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
        else:
            usuario_editar = {'form':form}
            return render(request, 'usuarios/edita_usuario.html', usuario_editar)
    else:
        form = cadastroClienteForms(instance=usuario)
    usuario_editar = {'form':form}
    return render(request, 'usuarios/edita_usuario.html', usuario_editar)

@login_required
@staff_member_required
def deleta_usuario(request):
    pass