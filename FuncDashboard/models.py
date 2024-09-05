from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from UserAutenticacao.models import Usuario
import uuid

# Create your views here.

#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
    
class Sobre(models.Model):
    texto="Somos uma lavandaria com um sistema totalmente diferenciado no mercado angolano, a maior parte das lavandarias no país, o que elas fazem não é serviço de lavandaria, mas de tinturaria, Pois oferecemos serviços de lavagem, secagem e engomagem de forma conjunta bem como segregada, por intermédio de cestos de roupas tu consegues fazer a lavagem, secagem ou engomagem de suas roupas em nossas lavandaria.Aqui a lavagem é feita em quantidade, pois acreditamos que o custo de lavagem de produção de uma única lavagem é o mesmo em quantidade."
    titulo = models.CharField(max_length=20, default='Sobre a Empresa', verbose_name='Título')
    descricao = models.TextField(max_length=20, default=texto, verbose_name='Descrição')

    
    class Meta:
        db_table = 'Sobre'
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'
    
    def __str__(self):
        return self.titulo
    

class Funcionario(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=20, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=20, verbose_name='Endereço')
    numero = models.CharField(max_length=9, verbose_name='Número de Tel')
    genero = models.CharField(max_length=9, choices=GENERO , verbose_name='Genero')
    img = models.ImageField(upload_to='Func/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Funcionario')
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
    img = models.ImageField(default="", upload_to='Servicos/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], verbose_name='Foto do Serviço')

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
    obs = models.TextField(null=True, blank=True)
    codigo_reserva = models.CharField(max_length=10, unique=True, editable=False)
    
    
    def save(self, *args, **kwargs):
        if not self.codigo_reserva:
            self.codigo_reserva = str(uuid.uuid4())
        super().save(*args, **kwargs)


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
        verbose_name = 'Serviço Reservado'
        verbose_name_plural = 'Serviços Reservados'    

    
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
        return f"{self.dataPagamento.strftime('%d/%m/%Y')}"
    

class Feedback(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    avaliacao = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Avaliação (1 a 5)')
    comentario = models.TextField(blank=True, null=True, verbose_name='Comentário')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data do Feedback')

    class Meta:
        db_table = 'Feedback'
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f"Feedback de {self.cliente}"
    

class ReservaEstatistica(models.Model):
    mes = models.DateField()
    estado = models.IntegerField()
    quantidade = models.IntegerField(default=0)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Funcionario')

    class Meta:
        unique_together = ('mes', 'estado','funcionario')
        db_table = 'reserva_estatistica'
        verbose_name = 'Estatística de Reserva'
        verbose_name_plural = 'Estatísticas de Reservas'

    def __str__(self):
        return f"{self.mes.strftime('%Y-%m')} - Estado: {self.estado} - Quantidade: {self.quantidade}"
