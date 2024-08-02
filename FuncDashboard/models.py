from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from UserAutenticacao.models import Usuario
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your views here.

#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
    
class Funcionario(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço')
    numero = models.CharField(max_length=9, verbose_name='Número de Tel')
    genero = models.CharField(max_length=9, choices=GENERO , verbose_name='Genero')
    img = models.ImageField(upload_to='Func/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')


    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero', 'img','usuario','loja']
    
    class Meta:
        db_table = 'Funcionario'
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
    
    def __str__(self):
        return self.nome
    

class Servico(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome Do Serviço')
    descricao = models.TextField(verbose_name='Descrição Do Serviço')
    preco = models.DecimalField(default=0.0,max_digits=10, decimal_places=2, verbose_name='Descrição Do Serviço')
    img = models.ImageField(upload_to='servico/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')

    REQUIRED_FIELDS = ['nome', 'descricao', 'preco' , 'img']

    class Meta:
        db_table = 'Servico'
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome

# Create your models here.
class Cliente(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço', null=True)
    email = models.EmailField(unique=True)
    numero = models.CharField(max_length=9, verbose_name='Número de Tel', null=True)
    genero = models.CharField(max_length=2, choices=GENERO , verbose_name='Genero')

    REQUIRED_FIELDS = ['nome', 'endereco', 'numero', 'genero']

    class Meta:
        unique_together = ('email', 'numero')
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
    estado = models.IntegerField(default=0, max_length=1)
    data_entrada = models.DateField(null=True)
    data_saida = models.DateField(null=True)
    obs = models.TextField(null=True)
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
        return f"reserva em {self.data_reserva} - Cliente: {self.cliente} - Total: {self.total} - Estado: {self.estado}"

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

    
class MetodoPagamento (models.Model):
    metodo = models.CharField(max_length=10)
    class Meta:
        db_table = 'MetodoPagamento'
        verbose_name = 'Metodo de Pagamento'
        verbose_name_plural = 'Metodos de Pagamentos'
    
    def __str__(self):
        return self.metodo

class Pagamentos (models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dataPagamento = models.DateField(auto_now_add=True)
    metodoPagamento = models.ForeignKey(MetodoPagamento, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Pagamento'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
    
    def __str__(self):
        return self.dataPagamento