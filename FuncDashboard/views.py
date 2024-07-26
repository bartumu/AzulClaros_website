from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Portifolio.models import *
from FuncDashboard.forms import *
from django.http import HttpResponse

# Create your views here.
def FuncDashboard(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            FuncObj = Funcionario.objects.get(usuario=request.user)
            usuario = request.user
            context = {
                'usuario':usuario,
                'Func':FuncObj
            }
            return render(request,'BackEnd/home.html', context)
        else:
            
            return redirect('Regperfil')
    return redirect('login')

def perfil_view(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            if request.method == 'GET':
                formCadastrar = FormCadFuncionario
                FuncObj = Funcionario.objects.get(usuario=request.user or None)
            
            
            if request.method == 'POST':
                formCadastrar = FormCadFuncionario(request.POST)
                if formCadastrar.is_valid():
                    img = formCadastrar.cleaned_data.get('img')
                    Func = formCadastrar.save(commit=False)
                    Func.img = img
                    Func.usuario = request.user
                    Func.save()
                    return redirect('marcacao')

            context = {
                'formCadastrar':formCadastrar,
                'Func':FuncObj
            }
            return render(request, 'BackEnd/Perfil/PerfilPag.html', context)
        return redirect('Regperfil')
    return redirect('login')

def marcacao_view(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            reservas = Reserva.objects.filter(estado=False)
            tem_reservas = Reserva.objects.exists()

            context = {
                'Reservas':reservas,
                'tem_reservas':tem_reservas,
                'usuario':request.user
            }

            return render(request,'BackEnd/Marcacao.html', context)
        return redirect('Regperfil')
    return redirect('login')

def atender_view(request,idReserva):
    
    if request.method == 'POST':
       reservas = get_object_or_404(Reserva,id=idReserva)
       func = get_object_or_404(Funcionario, usuario=request.user)
       atenderF = FormAtender(request.POST) 
       if atenderF.is_valid():
            data_saida = atenderF.cleaned_data.get('data_saida')

            print(reservas.cliente,reservas.estado,reservas.codigo_reserva, reservas.data_entrada)
            reservas.data_saida = data_saida
            reservas.total = Calcular_Total(idReserva)
            reservas.estado = True
            reservas.funcionario = func
            reservas.save()

            
            return redirect('marcacao')
       else:
           return HttpResponse("Formulário invalido", status=400)
    else:
        Total = Calcular_Total(idReserva)
        atenderF = FormAtender()
       
    context = {
        'Total': Total,
        'FormAtender': atenderF
    }
    return render(request,'BackEnd/Marcacao.html', context)



def logout_view(request):
    logout(request)
    messages.success(request,f"Logout Feito Com sucesso")
    return redirect('login')

def Calcular_Total(idReserva):
    return sum(servico.subtotal for servico in ServicosReservado.objects.filter(reserva=idReserva))

def RegistarPerfil(request):
    if request.method == 'POST':
        usuario = request.user
        formCadastrar = FormCadFuncionario(request.POST, request.FILES)
        if formCadastrar.is_valid():
            img = request.FILES['img']
            print(img)
            Func = formCadastrar.save(commit=False)
            Func.img = img
            Func.usuario = request.user
            Func.save()
            return redirect('marcacao')
    else:
        formCadastrar = FormCadFuncionario()
        usuario = request.user


    context = {
        'formCadastrar':formCadastrar,
        'usuario':usuario
    }
    return render(request,'BackEnd/Perfil/RegistarPerfil.html', context)