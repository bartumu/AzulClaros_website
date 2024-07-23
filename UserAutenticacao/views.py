from django.shortcuts import redirect, render
from UserAutenticacao.forms import FormRegistarUser
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .models import Usuario
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
            messages.add_message(request, messages.INFO, 'Mensagem de sucesso!')
            return redirect('FuncDashBoard')
        else:
            messages.warning(request, "Usuario não existe crie uma conta")
            return redirect('login')
        

        context = {}
    return render(request, 'Autenticacao/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,f"Logout Feito Com sucesso")
            
    return redirect('home')
