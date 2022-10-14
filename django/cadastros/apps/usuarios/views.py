import time
from django.shortcuts import render
from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from usuarios.models import Mensagens
from firebase_admin.messaging import Message, Notification, WebpushNotification, WebpushConfig
from fcm_django.models import FCMDevice
from django.views.generic import View


class ServiceWorkerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'notificacoes/firebase-messaging-sw.js', content_type="application/x-javascript")

def testeee(request):
    return render(request, 'notificacoes/teste.html')

def devices(request):
    """Realiza o cadastro de dispositivos de usuários"""
    if request.method == 'POST':
        registration_id = request.POST['registration_id']
        typee = request.POST['web']
        user = get_object_or_404(User, pk=request.user.id)
        name = user.username
        device = FCMDevice.objects.create(registration_id=registration_id, type=typee, user=user, name=name)
        device.save()
        return redirect('index')

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


def teste(request):
    mensagens = Mensagens.objects.order_by('-data_criacao').filter(habilitada=True)
    x = 0
    device = FCMDevice.objects.all().first()
    # device.send_message(Message(notification=Notification(title='comida', body='comida', image='https://blog.consumer.com.br/wp-content/uploads/2020/11/culin%C3%A1ria-regional-brasileira.jpg')))
    # device.send_message(Message(webpush=WebpushConfig(notification=WebpushNotification(title='comida', body='comida', image='https://blog.consumer.com.br/wp-content/uploads/2020/11/culin%C3%A1ria-regional-brasileira.jpg', icon='https://universo.adami.com.br/static/user/assets/images/logo_universo.png'))))
    for mensagem in mensagens:
        icone = ''
        if mensagem.icon:
            icone = mensagem.icon.url
        else:
            icone = 'https://universo.adami.com.br/static/user/assets/images/logo_universo.png'
        device.send_message(Message(webpush=WebpushConfig(notification=WebpushNotification(title=mensagem.titulo, body=mensagem.corpo_mensagem, image=mensagem.icon.url, icon=icone))))
         
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