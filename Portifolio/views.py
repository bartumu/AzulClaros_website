from django.shortcuts import render,redirect
from .forms import *
from.models import *

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'Portifolio/index.html')

def sobre(request):
    return render(request,'Portifolio/SobreNos.html')



def pedido(request):
        reserva = request.session.get('reserva')
        context = {
            'reserva':reserva
        }
        return render(request,'Portifolio/Pedido.html', context)


def addPedido_view(request):
    
    if request.method == 'POST':
         formCliente = FormRegistarCliente(request.POST)
         formReserva = FormFazerReserva(request.POST)
         formServicosReservados = FormReservaServico(request.POST)
         
         if formCliente.is_valid():
            cliente = formCliente.save()

            if formReserva.is_valid():
                reserva = formReserva.save(commit=False)
                reserva.cliente = cliente
                reserva.save()
                
            
                if formServicosReservados.is_valid():

                    servicosReservado = formServicosReservados.cleaned_data.get('servicos')
                    qtd = formServicosReservados.cleaned_data.get('qtd')

                    for servico in servicosReservado:
                        print(servico)
                        subtotal = servico.preco * qtd
                        total = 0 + subtotal
                        ServicosReservado.objects.create(
                            servico=servico,
                            reserva=reserva,
                            subtotal=subtotal,
                            qtd=qtd
                        )
                        """ servicosReservado = formServicosReservados.save(commit=False)
                        servicosReservado.reserva = reserva
                        servicosReservado.servico = servico
                        servicosReservado.subtotal = subtotal
                        servicosReservado.save() """
                        #reserva.atualizar_total()

                    reserva = request.session['reserva'] = reserva.codigo_reserva
                    return redirect("pedido")
            
    else:
        formReserva = FormFazerReserva()
        formCliente = FormRegistarCliente()
        formServicosReservados = FormReservaServico()
              

    context = {
         'formReserva' : formReserva,
         'FormCliente': formCliente,
         'FormServicosReservados': formServicosReservados,
         'Existe_servico': Existe_servico()
    }

    return render(request, 'Portifolio/PedidoAdd.html', context)

def Existe_servico():
    if Servico.objects.exists():
        return True
    else:
        return False
    