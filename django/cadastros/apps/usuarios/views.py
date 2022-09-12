from django.shortcuts import render
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *

def cadastro_usuario(request):
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