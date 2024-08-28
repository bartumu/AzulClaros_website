from django.shortcuts import redirect, render
from UserAutenticacao.forms import FormRegistarUser
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .models import Usuario
from Portifolio.views import Enviar_fatura_email
from threading import Thread
# Create your views here.

#Usuario = settings.AUTH_USER_MODEL


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            messages.warning(request, f"Usuário com email {email} não existe.")
            return redirect('login')

        usuario = authenticate(request, username=email, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, f"Bem-vindo {usuario.username}!")
            return redirect('FuncDashBoard')
        else:
            messages.warning(request, "Senha incorreta ou conta não existe.")
            return redirect('login')

    return render(request, 'Autenticacao/login.html')

def recuperar_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Recuperação da Senha | Azul Claros'
        html = 'Autenticacao/Email/EmailRecuperar.html'
        context = {
            'email': email
        }
        Thread(target=Enviar_fatura_email, args=(html, subject, context, email)).start()
        messages.success(request, 'Email de recuperação enviado.')
        return redirect('login')
    return render(request, 'Autenticacao/recuperar.html')

def recuperar_senha(request):
    if request.method == 'POST':
        email = request.GET.get("email")
        senha = request.POST.get("password")
        senhaConf = request.POST.get("password_confirm")
        if senha == senhaConf:
            try:
                user = Usuario.objects.get(email=email)
                user.set_password(senhaConf)
                user.save()
                messages.success(request, 'Senha atualizada com sucesso.')
                return redirect('login')
            except Usuario.DoesNotExist:
                messages.warning(request, 'Usuário não encontrado.')
                return redirect('recuperarSenha')
        else:
            messages.warning(request, 'As senhas não coincidem.')

    return render(request, 'Autenticacao/recuperarSenha.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logout feito com sucesso.")
    return redirect('login')