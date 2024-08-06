import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .models import *
from datetime import date, timedelta

def reservas_por_estadoJS():
    FuncObj = Funcionario.objects.all()
    today = date.today()
    start_date = today.replace(day=1)
    end_date = today

    # Filtrar reservas no intervalo de datas
    reservas = Reserva.objects.filter(data_reserva__range=[start_date, end_date])

    # Contar as reservas por estado
    counts = [
        reservas.filter(estado=0).count(),  # Pendente
        reservas.filter(estado=1).count(),  # Em Processamento
        reservas.filter(estado=2).count()   # Atendidos
    ]

    return counts
def reservas_por_estadoJS(request):
    FuncObj = Funcionario.objects.get(usuario=request.user)
    today = date.today()
    start_date = today.replace(day=1)
    end_date = today

    # Filtrar reservas no intervalo de datas
    reservas = Reserva.objects.filter(data_reserva__range=[start_date, end_date])

    # Contar as reservas por estado
    counts = [
        reservas.filter(estado=0).count(),  # Pendente
        reservas.filter(estado=1, funcionario_id=FuncObj.id).count(),  # Em Processamento
        reservas.filter(estado=2, funcionario_id=FuncObj.id).count()   # Atendidos
    ]

    return counts

def reservas_por_estado():
    today = date.today()
    start_date = today.replace(day=1)
    end_date = today

    # Filtrar reservas no intervalo de datas
    reservas = Reserva.objects.filter(data_reserva__range=[start_date, end_date])

    # Contar as reservas por estado
    estados = ['Pendente', 'Em Processamento', 'Atendidos']
    counts = [reservas.filter(estado=i).count() for i in range(3)]

    # Gerar o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(counts, labels=estados, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('')

    # Salvar o gráfico em um buffer
    #buf = io.BytesIO()
    plt.savefig('static/Relactorios/reservas_por_estado.png')

def gerar_relatorio_PorFunc(request):
    # Coletar dados
    funcionario = Funcionario.objects.get(usuario=request.user)
    pagamentos = Pagamentos.objects.all()

    # Estruturar dados em DataFrames
    dados_funcionarios = {
        'nome': [],
        'total_reservas': [],
        'total_pagamentos': []
    }
    print(funcionario.id)
    #for funcionario in funcionarios:
    total_reservas = Reserva.objects.filter(funcionario_id=funcionario.id).count()
    total_pagamentos = sum(p.valor for p in Pagamentos.objects.filter(reserva__funcionario=funcionario))

    dados_funcionarios['nome'].append(funcionario.nome)
    dados_funcionarios['total_reservas'].append(total_reservas)
    dados_funcionarios['total_pagamentos'].append(total_pagamentos)

    df_funcionarios = pd.DataFrame(dados_funcionarios)

    # Criar visualizações
    plt.figure(figsize=(10, 6))
    sns.barplot(x='nome', y='total_reservas', data=df_funcionarios)
    plt.title('Total de Reservas por Funcionário')
    plt.xlabel('Funcionário')
    plt.ylabel('Total de Reservas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/total_reservas_por_funcionario.png')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='nome', y='total_pagamentos', data=df_funcionarios)
    plt.title('Total de Pagamentos por Funcionário')
    plt.xlabel('Funcionário')
    plt.ylabel('Total de Pagamentos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/Relactorios/total_pagamentos_por_funcionario.png')

def gerar_relatorio():
    # Coletar dados
    funcionarios = Funcionario.objects.all()
    pagamentos = Pagamentos.objects.all()

    # Estruturar dados em DataFrames
    dados_funcionarios = {
        'nome': [],
        'total_reservas': [],
        'total_pagamentos': []
    }

    for funcionario in funcionarios:
        total_reservas = funcionario.func.all().count()
        total_pagamentos = sum(p.valor for p in Pagamentos.objects.filter(reserva__funcionario=funcionario))

        dados_funcionarios['nome'].append(funcionario.nome)
        dados_funcionarios['total_reservas'].append(total_reservas)
        dados_funcionarios['total_pagamentos'].append(total_pagamentos)

    df_funcionarios = pd.DataFrame(dados_funcionarios)

    # Criar visualizações
    plt.figure(figsize=(10, 6))
    sns.barplot(x='nome', y='total_reservas', data=df_funcionarios)
    plt.title('Total de Reservas por Funcionário')
    plt.xlabel('Funcionário')
    plt.ylabel('Total de Reservas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/Relactorios/total_reservas_por_funcionario.png')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='nome', y='total_pagamentos', data=df_funcionarios)
    plt.title('Total de Pagamentos por Funcionário')
    plt.xlabel('Funcionário')
    plt.ylabel('Total de Pagamentos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/Relactorios/total_pagamentos_por_funcionario.png')


def gerar_analise_vendas_por_servico():
    # Coletar dados
    servicos_reservados = ServicosReservado.objects.all()

    # Estruturar dados em DataFrame
    dados_vendas = {
        'servico': [],
        'total_vendas': [],
        'receita': []
    }

    for servico in Servico.objects.all():
        total_vendas = servicos_reservados.filter(servico=servico).count()
        receita = sum(sr.subtotal for sr in servicos_reservados.filter(servico=servico))

        dados_vendas['servico'].append(servico.nome)
        dados_vendas['total_vendas'].append(total_vendas)
        dados_vendas['receita'].append(receita)

    df_vendas = pd.DataFrame(dados_vendas)

    # Criar visualizações
    plt.figure(figsize=(10, 6))
    sns.barplot(x='servico', y='total_vendas', data=df_vendas)
    plt.title('Total de Vendas por Serviço')
    plt.xlabel('Serviço')
    plt.ylabel('Total de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/Relactorios/total_vendas_por_servico.png')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='servico', y='receita', data=df_vendas)
    plt.title('Receita por Serviço')
    plt.xlabel('Serviço')
    plt.ylabel('Receita')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/Relactorios/receita_por_servico.png')