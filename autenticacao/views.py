from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirma_senha = request.POST.get('confirmar_senha')
    
        if not password_is_valid(request, senha, confirma_senha):
            return redirect('/auth/cadastro')
    
        return HttpResponse('Testando')

def logar(request):
    return HttpResponse('Você está na página de login')