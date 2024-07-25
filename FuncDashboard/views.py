from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Portifolio.models import *
from FuncDashboard.forms import *

# Create your views here.
def FuncDashboard(request):
    usuario = request.user
    context = {
        'usuario':usuario
    }
    return render(request,'BackEnd/home.html', context)

def perfil_view(request):

    if request.method == 'GET':
        formCadastrar = FormCadFuncionario
        context = {
            'formCadastrar':formCadastrar
        }

    return render(request, 'BackEnd/Perfil/PerfilPag.html', context)

def marcacao_view(request):
    reservas = Reserva.objects.all()
    tem_reservas = Reserva.objects.exists()

    context = {
        'Reservas':reservas,
        'tem_reservas':tem_reservas
    }

    return render(request,'BackEnd/Marcacao.html', context)

def logout_view(request):
    logout(request)
    messages.success(request,f"Logout Feito Com sucesso")
    return redirect('login')


