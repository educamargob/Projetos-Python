from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(nome):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if verifica_senhas(senha, senha2):
            messages.error(request, 'As senhas não correspondem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    """Realiza o login de uma pessoa no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == "" or senha == "":
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        
    return render(request, 'usuarios/login.html')

def logout(request):
    """Realiza o logout de uma pessoa no sistema"""
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """Mostra na tela as receitas do usuário"""
    if request.user.is_authenticated :
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    """CADASTRO -- Verificar se o campo esta vazio"""
    return not campo.strip()
    
def verifica_senhas(senha, senha2):
    """CADASTRO -- Verificar senhas de cadastro"""
    return senha != senha2

