from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from UserAutenticacao.models import Usuario
from phonenumber_field.modelfields import PhoneNumberField
# Create your views here.

#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome Do Serviço')
    descricao = models.CharField(max_length=20, verbose_name='Descrição Do Serviço')
    preco = models.DecimalField(default=0.0,max_digits=10, decimal_places=2, verbose_name='Descrição Do Serviço')
    img = models.ImageField(upload_to='servico/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')

    REQUIRED_FIELDS = ['nome', 'descricao', 'preco' , 'img']

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço')
    numero = PhoneNumberField(max_length=9, region='AO', verbose_name='Número de Tel')
    genero = models.CharField(max_length=9, choices=GENERO , verbose_name='Genero')
    img = models.ImageField(upload_to='func/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')


    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero', 'img','usuario','loja']
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
    
    def __str__(self):
        return self.nome
    

