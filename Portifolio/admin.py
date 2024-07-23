from django.contrib import admin
from .forms import CliForm
from .models import *


# Register your models here.

class CliAdmin(admin.ModelAdmin):
    form = CliForm
    list_display=['nome','genero', 'endereco' ]

admin.site.register(Cliente, CliAdmin)