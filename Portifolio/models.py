from django.db import models
from AdminDashboard.models import *


# Create your models here.

class Pedido (models.Model):
    data_pedido = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='pedido_loja')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='func')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cli')
    estado = models.BooleanField()
    data_entrada = models.DateField()
    data_saida = models.DateField()

    def __str__(self):
        return f"Pedido em {self.data_pedido} - Cliente: {self.cliente} - Total: {self.total} - Estado: {self.estado} Na Loja: {self.loja}"

class ItemPedido (models.Model):
    qtd = models.IntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedido')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='servico')

    def __str__(self):
        return f"Pedido: {self.pedido}, Serviço: {self.servico}, Quantidade: {self.qtd}"

