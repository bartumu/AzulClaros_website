from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FuncDashboard.models import *
from .forms import FuncForm
from django.urls import path
from FuncDashboard.relactorio import *
from django.shortcuts import render


class MetodoPagamentoAdmin(admin.ModelAdmin):
    list_display=['metodo']

class FuncAdmin(admin.ModelAdmin):
    form = FuncForm
    list_display=['nome','genero', 'endereco']

class CliAdmin(admin.ModelAdmin):
    list_display=['nome','genero', 'endereco' ]

class ServicoAdmin(admin.ModelAdmin):
    list_display=['nome','descricao','preco']

class ReservaAdmin(admin.ModelAdmin):
    list_display=['cliente','codigo_reserva','data_entrada','data_saida','total','funcionario']

class PagamentoAdmin(admin.ModelAdmin):
    list_display=['reserva','dataPagamento','metodoPagamento','valor']

class ReservaEstatisticaAdmin(admin.ModelAdmin):
    list_display=['funcionario','estado','mes','quantidade']

class FeedBackAdmin(admin.ModelAdmin):
    list_display=['cliente','comentario','avaliacao','data']

class SobreAdmin(admin.ModelAdmin):
    list_display=['titulo','descricao']

class ServicosReservadoAdmin(admin.ModelAdmin):
    list_display=['reserva','subtotal','qtd','servico']


admin.site.register(Cliente, CliAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Funcionario, FuncAdmin)
admin.site.register(MetodoPagamento, MetodoPagamentoAdmin)
admin.site.register(Pagamentos, PagamentoAdmin)
admin.site.register(ReservaEstatistica, ReservaEstatisticaAdmin)
admin.site.register(Feedback, FeedBackAdmin)
admin.site.register(Sobre, SobreAdmin)
admin.site.register(ServicosReservado, ServicosReservadoAdmin)
# Register your models here.
