from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from Portifolio.models import *
from FuncDashboard.forms import *
from django.http import HttpResponse, JsonResponse
from datetime import date
from django.db.models import Sum, Count
from FuncDashboard.relactorio import *
from datetime import date, timedelta
from Portifolio.views import Enviar_fatura_email
from threading import Thread
from django.utils.safestring import mark_safe
import json

# Create your views here.
def FuncDashboard(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            FuncObj = Funcionario.objects.get(usuario=request.user)
            reservas = Reserva.objects.filter(estado=2, funcionario_id=FuncObj.id)
            reservaPendente = Reserva.objects.filter(estado=0).count()
            reservaProc = Reserva.objects.filter(estado=1).count()
            tem_reservas = Reserva.objects.filter(estado=2).exists()
            clientes = Cliente.objects.count()
            ChartRes = mark_safe(json.dumps(preparar_dados_grafico(request)))
            percentagemCli = 0
            percentagemReserva = 0
            percentagemProc = 0
            if clientes!=0: 
                percentagemCli = (reservas.count() * 100) // clientes
            if reservaProc!=0: 
                percentagemReserva = (reservaPendente * 100) // reservaProc
            if reservaPendente!=0:
                percentagemProc = (reservaProc * 100)//reservaPendente
            


            print(reservas.aggregate(Sum('total'))['total__sum'])
            context = {
                'Reservas':reservas,
                'tem_reservas':tem_reservas,
                'CliPercentagem': percentagemCli,
                'percentagemReserva': percentagemReserva,
                'percetagemProc': percentagemProc,
                'CliAtendido': reservas.count(),
                'reservaPendente': reservaPendente,
                'reservaProc': reservaProc,
                'usuario':request.user,
                'reservas_por_estado': 'Relactorios/reservas_por_estado.png',
                'ResChart': ChartRes,
                'Func': FuncObj
            }

            return render(request,'BackEnd/home.html', context)
        return redirect('Regperfil')
    return redirect('login')

#
def listReserva_view(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            formPagamento = FormPagamento()
            reservas = Reserva.objects.filter(estado=False)
            tem_reservas = Reserva.objects.filter(estado=0).exists()
            FuncObj = Funcionario.objects.get(usuario=request.user)

            context = {
                'Reservas':reservas,
                'tem_reservas':tem_reservas,
                'usuario':request.user,
                'FormPagamento':formPagamento,
                'Func': FuncObj,
                'reservaPendente' : Reserva.objects.filter(estado=0).count(),
                'reservaProc' : Reserva.objects.filter(estado=1).count(),
            }

            return render(request,'BackEnd/ListReservas.html', context)
        return redirect('Regperfil')
    return redirect('login')

def Levantamento_view(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            formPagamento = FormPagamento()
            reservas = Reserva.objects.filter(estado=1)
            tem_reservas_Sair = Reserva.objects.filter(estado=1).exists()
            FuncObj = Funcionario.objects.get(usuario=request.user)
            reservaPendente = Reserva.objects.filter(estado=0).count()
            reservaProc = Reserva.objects.filter(estado=1).count()

            context = {
                'reservaPendente':reservaPendente,
                'reservaProc':reservaProc,
                'Reservas':reservas,
                'tem_reservas_Sair':tem_reservas_Sair,
                'usuario':request.user,
                'FormPagamento':formPagamento,
                'Func': FuncObj,
            }

            return render(request,'BackEnd/Levantamento.html', context)
        return redirect('Regperfil')
    return redirect('login')

def atender_view(request,idReserva):
    
    if request.method == 'POST':
       reservas = get_object_or_404(Reserva,id=idReserva)
       func = get_object_or_404(Funcionario, usuario=request.user)
       formPagamento = FormPagamento(request.POST)
       atenderF = FormAtender(request.POST) 
       if atenderF.is_valid():
            data_saida = atenderF.cleaned_data.get('data_saida')

            print(reservas.cliente,reservas.estado,reservas.codigo_reserva, reservas.data_entrada)
            reservas.data_saida = data_saida
            reservas.total = Calcular_Total(idReserva)
            reservas.estado = True
            reservas.funcionario = func
            reservas.save()
            if formPagamento.is_valid():
                Pag = formPagamento.save(commit=False)
                Pag.reserva = reservas
                Pag.valor = Calcular_Total(idReserva)
                Pag.save()

                # Envio do email ao cliente
                subject = 'Factura | Azul Claros'
                cliente_email = reservas.cliente.email
                html = 'BackEnd/Cliente/FacturaPag.html'
                context = {
                    'Reserva': Reserva.objects.get(id=reservas.id),
                    'servicosReservados': ServicosReservado.objects.filter(reserva=reservas),
                    'Pagamento': Pagamentos.objects.get(reserva=reservas)
                }
                Thread(target=Enviar_fatura_email, args=(html,subject, context, cliente_email)).start()
                messages.success(request, f'{ reservas.cliente.nome } atendido com sucesso e notificado por Email')
                return redirect('reserva')
       else:
                messages.warning(request, 'Verifique a Data de Saida')
                return redirect('reserva')
    else:
        Total = Calcular_Total(idReserva)
        atenderF = FormAtender()
        formPagamento = FormPagamento()
       
    context = {
        'reservaPendente' : Reserva.objects.filter(estado=0).count(),
        'reservaProc' : Reserva.objects.filter(estado=1).count(),
        'FormAtender': atenderF,
        'FormPagamento':formPagamento
    }
    return render(request,'BackEnd/ListReserva.html', context)

def levantar_view(request,idReserva):
    
    if request.method == 'POST':
       reservas = get_object_or_404(Reserva,id=idReserva)
       func = get_object_or_404(Funcionario, usuario=request.user)
       levantarF = FormAtender(request.POST) 
       #data_Hoje = levantarF.cleaned_data.get('data_saida')
       data_saida_BD = reservas.data_saida
       data_Hoje = date.today()
       print("Passou aqui")
       if data_saida_BD == data_Hoje:
            reservas.estado = 2
            reservas.funcionario = func
            reservas.save()
            messages.success(request, f'{ reservas.cliente.nome } atendido com sucesso.')

       else:
            reservas.data_saida=data_Hoje
            reservas.estado = 2
            reservas.funcionario = func
            reservas.save()
            messages.success(request, f'{ reservas.cliente.nome } atendido com sucesso.')
            return redirect('levantamento')
    else:
        levantarF = FormAtender
       
    context = {
        'FormLevantar': levantarF,
    }
    return render(request,'BackEnd/Levantamento.html', context)

def logout_view(request):
    logout(request)
    messages.success(request,f"Logout Feito Com sucesso")
    return redirect('login')

def Calcular_Total(idReserva):
    return sum(servico.subtotal for servico in ServicosReservado.objects.filter(reserva=idReserva))

def RegistarPerfil(request):
    EditarPerfil = False
    
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario=request.user).exists():
            funcionario = Funcionario.objects.get(usuario_id=request.user)
            usuario = funcionario.usuario

            if request.method == 'POST':
                form = FuncionarioPerfilForm(request.POST, request.FILES, instance=funcionario, user=usuario)
                if form.is_valid():
                    form.save()
                    return redirect('perfil')
            else:
                form = FuncionarioPerfilForm(instance=funcionario, user=usuario)

            return render(request, 'BackEnd/Perfil/PerfilPag.html', {'form': form,'Func':funcionario})
        else:
            formCadastrar = FormCadFuncionario()
            usuario = request.user

            if request.method == 'POST':
                usuario = request.user
                formCadastrar = FormCadFuncionario(request.POST, request.FILES)
                if formCadastrar.is_valid():
                    img = request.FILES['img']
                    Func = formCadastrar.save(commit=False)
                    Func.img = img
                    Func.usuario = request.user
                    Func.save()

                    messages.success(request, 'Perfil Criado Com Sucesso.')

                    return redirect('reserva')
                


            context = {
                'formCadastrar':formCadastrar,
                'usuario':usuario,
                'EditarPerfil':EditarPerfil,
                'Func':None
            }
            return render(request,'BackEnd/Perfil/RegistarPerfil.html', context)
    
    else:
        return redirect('login')

def RegistarCliente(request):
    return 'a'

def Relatorio(request):
    today = date.today()
    start_date = today.replace(day=1) 
    end_date = today 

    # Total de Clientes Atendidos no mês atual
    CliAtendido = Reserva.objects.filter(estado=2, data_reserva__range=[start_date, end_date]).count()

    # Filtrar reservas no intervalo de datas
    reservas = Reserva.objects.filter(data_reserva__range=[start_date, end_date])

    # Contar as reservas por estado
    counts = [
        reservas.filter(estado=0).count(),  # Pendente
        reservas.filter(estado=1).count(),  # Em Processamento
        reservas.filter(estado=2).count()   # Atendidos
    ]

    # Agregar os dados de pagamentos por serviço
    dados = ServicosReservado.objects.values('servico__nome').annotate(total=Sum('subtotal')).order_by('servico__nome')

    # Formatar os dados para o gráfico de vendas por serviço
    categorias = [item['servico__nome'] for item in dados]
    valores = [str(item['total']) for item in dados] 

    # Agregar os dados de reservas por funcionário (apenas as atendidas)
    dadosF = Reserva.objects.filter(estado=2, data_reserva__range=[start_date, end_date]).values('funcionario__nome').annotate(total=Count('id')).order_by('funcionario__nome')

    categoriasF = [item['funcionario__nome'] if item['funcionario__nome'] else "Desconhecido" for item in dadosF]
    valoresF = [str(item['total']) for item in dadosF]

    # Frequência de reservas por dia no mês atual
    reservas_por_dia = reservas.values('data_reserva').annotate(quantidade=Count('id')).order_by('data_reserva')

    # Convertendo a data para string
    reservas_por_dia = [
        {'data_reserva': item['data_reserva'].strftime('%Y-%m-%d'), 'quantidade': item['quantidade']}
        for item in reservas_por_dia
    ]
    # Frequência de reservas por cliente no mês atual
    reservas_por_cliente = reservas.values('cliente__nome').annotate(quantidade=Count('id')).order_by('-quantidade')

    # Filtrar reservas atendidas
    reservas_atendidas = Reserva.objects.filter(estado=2)

    # Calcular a receita total por mês
    receita_por_mes = reservas_atendidas.values('data_reserva__month').annotate(total_receita=Sum('total')).order_by('data_reserva__month')

    # Convertendo o mês para string e receita total
    receita_por_mes = [
        {'mes': item['data_reserva__month'], 'total_receita': float(item['total_receita'])}
        for item in receita_por_mes
    ]

    # Agrupar receitas por semana
    receita_por_semana = reservas_atendidas.extra(select={'semana': "EXTRACT(week FROM data_reserva)"}).values('semana').annotate(total_receita=Sum('total')).order_by('semana')

    receita_por_semana = [
        {'semana': item['semana'], 'total_receita': float(item['total_receita'])}
        for item in receita_por_semana
    ]

   # Mapeamento das expressões para as avaliações
    avaliacao_labels = {
        1: 'Péssimo',
        2: 'Mal',
        3: 'Bom',
        4: 'Muito Bom',
        5: 'Excelente'
    }

    # Agregando os dados de satisfação
    feedback_data = Feedback.objects.values('avaliacao').annotate(total=models.Count('avaliacao')).order_by('avaliacao')

    # Preparando os dados para o ApexCharts
    labelsS = [avaliacao_labels[data['avaliacao']] for data in feedback_data]
    seriesS = [data['total'] for data in feedback_data]


    context = dict(
        counts=counts,
        categorias=categorias,
        categoriasF=categoriasF,
        valoresF=valoresF,
        valores=valores,
        CliAtendido=CliAtendido,
        ValorVendido=reservas.filter(estado=2).aggregate(Sum('total'))['total__sum'],
        reservas_por_dia=list(reservas_por_dia),
        reservas_por_cliente=list(reservas_por_cliente),
        receita_por_mes= receita_por_mes,
        receita_por_semana= receita_por_semana,
        labelsS= labelsS,
        seriesS= seriesS
    )
    
    return render(request, 'Admin/Relactorios.html', context)


def obter_dados_estatisticas_reservas():
    estatisticas = ReservaEstatistica.objects.all().order_by('mes', 'estado')

    dados_por_mes = {}

    for estatistica in estatisticas:
        mes = estatistica.mes.strftime('%Y-%m')
        estado = estatistica.estado
        quantidade = estatistica.quantidade

        if mes not in dados_por_mes:
            dados_por_mes[mes] = {0: 0, 1: 0, 2: 0}

        dados_por_mes[mes][estado] = quantidade

    return dados_por_mes

def preparar_dados_grafico(request):
    func = Funcionario.objects.get(usuario=request.user)
    estatisticasPendente = ReservaEstatistica.objects.all().order_by('mes', 'estado')

    labels = []
    dados_pendentes = []
    dados_processamento = []
    dados_atendido = []

    for estatistica in estatisticasPendente:
        mes = estatistica.mes.strftime('%Y-%m')
        if mes not in labels:
            labels.append(mes)
        if estatistica.estado == 0:
            dados_pendentes.append(estatistica.quantidade)

    if ReservaEstatistica.objects.filter(funcionario=func.id).exists():
        estatisticas = ReservaEstatistica.objects.filter(funcionario=func.id).order_by('mes', 'estado')
        for estatistica in estatisticas:
            

            if estatistica.estado == 1:
                dados_processamento.append(estatistica.quantidade)
            elif estatistica.estado == 2:
                dados_atendido.append(estatistica.quantidade)
        
    

    return {
        'labels': labels,
        'datasets': [
            {
                'label': 'Pendentes',
                'backgroundColor': 'rgba(255, 99, 132, 0.4)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'data': dados_pendentes,
            },
            {
                'label': 'Em Processamento',
                'backgroundColor': 'rgba(54, 162, 235, 0.4)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'data': dados_processamento,
            },
            {
                'label': 'Atendido',
                'backgroundColor': 'rgba(75, 192, 192, 0.4)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'data': dados_atendido,
            }
        ]
    }
