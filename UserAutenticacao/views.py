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

def registar_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = FormRegistarUser(request.POST or None)
        if form.is_valid():
            novo_utilizador = form.save(commit=False)
            novo_utilizador.set_password(form.cleaned_data.get('password1'))
            novo_utilizador.save()

            email = form.cleaned_data.get("email")
            messages.success(request,f"Oi {email}, Sua Conta foi criada com sucesso ")
            novo_utilizador=authenticate(username=email, 
                                         password=form.cleaned_data.get('password1'))
            if novo_utilizador is not None:
                login(request, novo_utilizador)
                return redirect("home")
    else:
        form = FormRegistarUser()

    
    context = {
        'formulario':form,
    }
    return render(request, 'Autenticacao/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)

            
        except:
            messages.warning(request,f"Usuarios com {email} não existe")
            
        usuario = authenticate(request, username=email, password=password)

        if usuario is not None:

            login(request, usuario)
            messages.warning(request, f"Bem-Vindo { usuario.username }")
            return redirect('FuncDashBoard')
        else:
            messages.warning(request, "Usuario não existe crie uma conta")
            return redirect('login')
        

        context = {}
    return render(request, 'Autenticacao/login.html')

def recuperar_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Recuperação da Senha | Azul Claros'
        html = 'Autenticacao/Email/EmailRecuperar.html'
        context={
            'email':email
        }
        Thread(target=Enviar_fatura_email, args=(html,subject, context,email)).start()
        messages.success(request, 'Email De Recuperação Enviado')
        return redirect('login')
    return render(request, 'Autenticacao/recuperar.html')

def recuperar_senha(request):
    if request.method == 'POST':
        email = request.GET.get("email")
        senha = request.POST.get("password")
        senhaConf = request.POST.get("password_confirm")
        if senha == senhaConf:
            user = Usuario.objects.get(email=email)
            user.set_password(senhaConf)
            user.save()
            messages.warning(request,'Senha Actualizada com Sucesso')
            return redirect('login')
        else:
            messages.warning(request,'As Senhas São Diferentes')
    return render(request, 'Autenticacao/recuperarSenha.html')


def logout_view(request):
    logout(request)
    messages.success(request,f"Logout Feito Com sucesso")
            
    return redirect('login')
