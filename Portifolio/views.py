from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'is_logged':is_logged(request)
    }
    return render(request,'Portifolio/index.html', context)

def sobre(request):
    return render(request,'Portifolio/SobreNos.html')

def pedido(request):
    context = {
        'is_logged': is_logged(request)
    }
    if request.user.is_authenticated:
        return render(request,'Portifolio/Pedido.html', context)
    return redirect('login')

def addPedido_view(request):
    context = {
        'is_logged': is_logged(request)
    }
    return render(request, 'Portifolio/PedidoAdd', context)

def is_logged(request):
    if request.user.is_authenticated:
        return True
    else:
        return False