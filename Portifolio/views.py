from django.shortcuts import render,redirect
from .forms import FormFazerPedido, FormRegistarCliente

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
        return render(request,'Portifolio/Pedido.html')

def addPedido_view(request):

    formPedido = FormFazerPedido()
    formCliente = FormRegistarCliente()

    context = {
         'FormPedido' : formPedido,
         'FormCliente': formCliente
    }

    return render(request, 'Portifolio/PedidoAdd.html', context)

def is_logged(request):
    if request.user.is_authenticated:
        return True
    else:
        return False