from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FuncDashboard.models import *
from .forms import FuncForm








class MetodoPagamentoAdmin(admin.ModelAdmin):
    list_display=['metodo']

class FuncAdmin(admin.ModelAdmin):
    form = FuncForm
    list_display=['nome','genero', 'endereco']

class CliAdmin(admin.ModelAdmin):
    list_display=['nome','genero', 'endereco' ]

class ServicoAdmin(admin.ModelAdmin):
    list_display=['nome','descricao','preco']



admin.site.register(Cliente, CliAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Funcionario, FuncAdmin)
admin.site.register(MetodoPagamento, MetodoPagamentoAdmin)

# Register your models here.
