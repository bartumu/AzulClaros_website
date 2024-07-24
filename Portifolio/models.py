from django.db import models
from FuncDashboard.models import *
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Cliente(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço')
    numero = PhoneNumberField(max_length=9,region='AO', verbose_name='Número de Tel')
    genero = models.CharField(max_length=2, choices=GENERO , verbose_name='Genero')

    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero']

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Pedido (models.Model):
    data_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='func')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cli')
    qtd = models.IntegerField()
    estado = models.BooleanField()
    data_entrada = models.DateField()
    data_saida = models.DateField()


    def __str__(self):
        return f"Pedido em {self.data_pedido} - Cliente: {self.cliente} - Total: {self.total} - Estado: {self.estado} Na Loja: {self.loja}"

class ItemPedido (models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedido')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='servico')


    def __str__(self):
        return f"Pedido: {self.pedido}, Serviço: {self.servico}"

