from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from UserAutenticacao.models import Usuario
# Create your views here.

#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome Da Loja')
    #numero = models.PhoneNumberField(region='AO', verbose_name='Número de Tel')
    numero = models.IntegerField(max_length=9, verbose_name='Número de Tel')
    
    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome Do Serviço')
    descricao = models.CharField(max_length=20, verbose_name='Descrição Do Serviço')
    img = models.ImageField(upload_to='servico/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')

    REQUIRED_FIELDS = ['nome', 'descricao', 'img']

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço')
    numero = models.CharField(max_length=9, verbose_name='Numero de Tel')
    genero = models.CharField(max_length=9, choices=GENERO , verbose_name='Genero')
    img = models.ImageField(upload_to='func/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='loja', verbose_name='Loja')
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='funcUsuario', verbose_name='Usuario')


    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero', 'img','usuario','loja']
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço')
    numero = models.CharField(max_length=9, verbose_name='Numero de Tel')
    genero = models.CharField(max_length=2, choices=GENERO , verbose_name='Genero')
    dataNasc = models.DateField(verbose_name='Data de Nascimento')
    img = models.ImageField(upload_to='cli/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='cliUsuario', verbose_name='Usuario')

    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero', 'dataNasc', 'img', 'usuario']

    def __str__(self):
        return self.nome

