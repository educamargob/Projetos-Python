from django.shortcuts import render
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib import auth, messages
from .forms import *

def cadastro_usuario(request):
    if request.method == 'POST':
       form = cadastroClienteForms(request.POST, request.FILES)
       if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cadastroClienteForms()
        contexto = {
            'form':form
        }
        return render(request, 'usuarios/cadastro.html', contexto)