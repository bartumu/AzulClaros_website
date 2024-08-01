from django.contrib import admin
from UserAutenticacao.models import Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from UserAutenticacao.forms import *


class UserAdmin(BaseUserAdmin):
    list_display=['username','email','password']
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    fieldsets = (
        ('Segurança', {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('username',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1','password2'),
            'description': 'Preencha os campos abaixo para criar um novo usuário.'
        }),
    )

admin.site.register(Usuario, UserAdmin)
# Register your models here.
