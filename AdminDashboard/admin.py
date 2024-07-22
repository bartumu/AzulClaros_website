from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from AdminDashboard.models import Loja, Servico, Funcionario, Cliente,Usuario
from .forms import CliForm,FuncForm




class LojaAdmin(admin.ModelAdmin):
    list_display=['nome','numero']

class ServicoAdmin(admin.ModelAdmin):
    list_display=['nome','descricao']

class FuncAdmin(admin.ModelAdmin):
    form = FuncForm
    list_display=['nome','genero', 'endereco' ,'loja']

class CliAdmin(admin.ModelAdmin):
    form = CliForm
    list_display=['nome','genero', 'endereco' ]

admin.site.register(Servico, ServicoAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Funcionario, FuncAdmin)
admin.site.register(Cliente, CliAdmin)

# Register your models here.
