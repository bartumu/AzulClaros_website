from django.contrib import admin
from UserAutenticacao.models import Usuario

class UserAdmin(admin.ModelAdmin):
    list_display=['username','email','password']

admin.site.register(Usuario, UserAdmin)
# Register your models here.
