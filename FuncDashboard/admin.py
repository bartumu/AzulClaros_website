from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FuncDashboard.models import *
from .forms import FuncForm




class LojaAdmin(admin.ModelAdmin):
    list_display=['nome','numero']

class ServicoAdmin(admin.ModelAdmin):
    list_display=['nome','descricao']

class FuncAdmin(admin.ModelAdmin):
    form = FuncForm
    list_display=['nome','genero', 'endereco' ,'loja']



admin.site.register(Servico, ServicoAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Funcionario, FuncAdmin)

# Register your models here.
