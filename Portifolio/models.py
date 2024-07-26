from typing import Iterable
from django.db import models
import uuid
from FuncDashboard.models import *
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Cliente(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço', null=True)
    numero = models.CharField(max_length=9, verbose_name='Número de Tel', null=True)
    genero = models.CharField(max_length=2, choices=GENERO , verbose_name='Genero')

    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero']

    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Reserva (models.Model):
    data_reserva = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True, related_name='func')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    data_entrada = models.DateField(null=True)
    data_saida = models.DateField(null=True)
    codigo_reserva = models.CharField(max_length=10, unique=True, editable=False)
    
    def save(self):
        if not self.codigo_reserva:
            self.codigo_reserva=str(uuid.uuid4())
            return super().save()
        return super().save()
    
    def atualizar_total(self):
        total = sum(servico.subtotal for servico in self.reserva.all())
        self.total = total
        self.save()

    class Meta:
        db_table = 'Reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'


    def __str__(self):
        return f"reserva em {self.data_reserva} - Cliente: {self.cliente} - Total: {self.total} - Estado: {self.estado} Na Loja: {self.loja}"

class ServicosReservado (models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='reserva')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='servico')
    qtd = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)


    def __str__(self):
        return f"reserva: {self.reserva}, Serviço: {self.servico}"
    

    class Meta:
        db_table = 'ServicoReservado'
        verbose_name = 'ServicoReservado'
        verbose_name_plural = 'ServicoReservados'    

