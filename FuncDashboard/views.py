from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def FuncDashboard(request):
    usuario = request.user
    context = {
        'usuario':usuario
    }
    return render(request,'BackEnd/home.html', context)

def logout_view(request):
    logout(request)
    messages.success(request,f"Logout Feito Com sucesso")
    return redirect('login')


