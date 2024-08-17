from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import *
import json
from FuncDashboard.models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from threading import Thread
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def index(request):
    sobre = Sobre.objects.get()
    context = {
        "Sobre":sobre,
        "Tem_Sobre":Existe_servico(),
    }
    return render(request,'Portifolio/index.html', context)

def sobre(request):
    sobre = Sobre.objects.get()
    context = {
        "Sobre":sobre
    }
    return render(request,'Portifolio/SobreNos.html', context)

def servico(request):
    return render(request,'Portifolio/nossoServico.html')

def contacto(request):
    if request.method == 'POST':  
        form = FeedbackForm(request.POST)  
        if form.is_valid():  
            try:
                email = form.cleaned_data['email']  
                cliente = Cliente.objects.get(email=email)  
                
                feedback = form.save(commit=False)  
                feedback.cliente = cliente  
                feedback.save() 
                return redirect('home') 
            except:
                messages.warning(request, 'Faça no mínimo uma reserva para ser Apto a Dar FeedBack')
                return redirect('home')

    form = FeedbackForm() 

    context = {
        'Form': form
    }
    return render(request,'Portifolio/Contacto.html', context)


def buscar_reserva(request):
    reserva = None
    servicosReservados = []

    if request.method == 'POST':
        codigo_reserva = request.POST.get('codigo_reserva')
        try:
            reserva = Reserva.objects.get(codigo_reserva=codigo_reserva)
            servicosReservados = ServicosReservado.objects.filter(reserva=reserva)
        except Reserva.DoesNotExist:
            reserva = None

    context = {
        'Reserva': reserva,
        'servicoReservado': servicosReservados
    }
    return render(request, 'Portifolio/Reserva.html', context)

def buscarReserva(request, codigo_):
    
    try:
        reserva = Reserva.objects.get(id=codigo_)
        servicosReservados = ServicosReservado.objects.filter(reserva=reserva)
    except Reserva.DoesNotExist:
        reserva = None

    context = {
        'Reserva': reserva,
        'servicoReservado': servicosReservados
    }
    return render(request, 'Portifolio/Reserva.html', context)


def reserva(request):
        reserva=0
        servicosReservado=0
        context = {
            'Reserva':reserva,
            'servicoReservado':servicosReservado
        }
        return render(request,'Portifolio/Reserva.html', context)


def addReserva_view(request):
    
    if request.method == 'POST':
         formCliente = FormRegistarCliente(request.POST)
         formReserva = FormFazerReserva(request.POST)
         formServicosReservados = FormReservaServico(request.POST)
         
         
         if formCliente.is_valid():
            #tel = formCliente.clean_telefone()
            cliente = formCliente.save()
            """ cliente.numero = tel
            cliente.save() """

            if formReserva.is_valid():
                reserva = formReserva.save(commit=False)
                reserva.cliente = cliente
                reserva.save()
                
            
                if formServicosReservados.is_valid():

                    servicosReservado = formServicosReservados.cleaned_data.get('servicos')
                    qtd = formServicosReservados.cleaned_data.get('qtd')

                    for servico in servicosReservado:
                        
                        subtotal = servico.preco * qtd
                        ServicosReservado.objects.create(
                            servico=servico,
                            reserva=reserva,
                            subtotal=subtotal,
                            qtd=qtd
                        )

                    # Envio do email ao cliente
                    subject = 'Comprovante da sua Reserva | Azul Claros'
                    cliente_email = cliente.email
                    html = 'BackEnd/Cliente/ComprovEmail.html'
                    context = {
                        'Reserva': Reserva.objects.get(id=reserva.id),
                        'servicosReservados': ServicosReservado.objects.filter(reserva=reserva),
                        'Qtd':qtd
                    }
                    Thread(target=Enviar_fatura_email, args=(html,subject, context, cliente_email)).start()

                    messages.success(request, 'Reserva realizada com sucesso! O comprovante foi enviado para o seu email.')


                    resera = request.session['reserva_id'] = reserva.id      
                    return buscarReserva(request,resera)
            
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

    return render(request, 'Portifolio/ReservaAdd.html', context)

    
def gerarPDF(request, idReserva):
    reserva = Reserva.objects.get(id=idReserva)
    servicosReservados = ServicosReservado.objects.filter(reserva=reserva)

    template_path = 'BackEnd/Cliente/ComprovRes.html'
    context = {
        'Reserva': reserva,
        'servicosReservados': servicosReservados
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Reserva_{reserva.codigo_reserva}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Temos algum erro <pre>' + html + '</pre>')
    return response

def Existe_servico():
    if Servico.objects.exists():
        return True
    else:
        return False

def Enviar_fatura_email(html,subject, context, cliente_email):
    message = render_to_string(html, context)
    email = EmailMessage(subject, message, to=[cliente_email])
    email.content_subtype = 'html'
    email.send()

""" def save_pdf(template_src,context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None
    
def pdf():
    codigo = 00000
    template_path = 'BackEnd/Cliente/FacturaPag.html'
    context = {'codigo': '00000'}

    pdf_file = save_pdf(template_path, context)
    if pdf_file:
        file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs',f'Reserva_{codigo}.pdf') 
        with open(file_path, 'wb') as f:
            f.write(pdf_file)
        BaixarComprovante()
        return JsonResponse({'url':f'{settings.MEDIA_URL}pdfs/Reserva_{codigo}.pdf'})
    
    return HttpResponse('Erro Em gerar Pdf', status=500) 

def BaixarComprovante():
    response = pdf()
    if response.status_code == 200:
        response_data= json.loads(response.content)
        pdf_url = response_data.get('url')
        return redirect(pdf_url)
    else:
        return HttpResponse('Erro gerando PDF', status=500)
 """