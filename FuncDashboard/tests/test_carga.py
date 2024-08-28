from django.test import TestCase
from FuncDashboard.models import ServicosReservado, Reserva, Servico,Cliente, Funcionario, Usuario
from django.test import TestCase

class ServicosReservadoLoadTest(TestCase):
    
    def setUp(self):
        self.reserva = Reserva.objects.create(
            cliente=Cliente.objects.create(
                nome='Cliente Teste',
                endereco='Endereco Teste',
                email='cliente@example.com',
                numero='923456780',
                genero='M'
            ),
            funcionario=Funcionario.objects.create(
                nome='Funcionario Teste',
                endereco='Endereco Teste',
                numero='923456781',
                genero='M',
                usuario=Usuario.objects.create(email='usuario@example.com', password='password123')
            ),
            estado=0,
            data_entrada='2024-08-10',
            data_saida='2024-08-11'
        )
        self.servico = Servico.objects.create(
            nome='Lavagem',
            descricao='Lavagem simples',
            preco=100.0
        )

    def test_criar_servicos_reservados(self):
        for i in range(1000):  # Simular a criação de 1000 serviços reservados
            ServicosReservado.objects.create(
                reserva=self.reserva,
                servico=self.servico,
                qtd=1,
                subtotal=100.0
            )
        self.assertEqual(ServicosReservado.objects.count(), 1000)


class ReservaLoadTest(TestCase):
    
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Cliente Teste',
            endereco='Endereco Teste',
            email='cliente@example.com',
            numero='923456780',
            genero='M'
        )
        self.funcionario = Funcionario.objects.create(
            nome='Funcionario Teste',
            endereco='Endereco Teste',
            numero='923456781',
            genero='M',
            usuario=Usuario.objects.create(email='usuario@example.com', password='password123')
        )

    def test_criar_reservas(self):
        for i in range(1000):  # Simular a criação de 1000 reservas
            Reserva.objects.create(
                cliente=self.cliente,
                funcionario=self.funcionario,
                estado=i % 3,
                data_entrada='2024-08-10',
                data_saida='2024-08-11'
            )
        self.assertEqual(Reserva.objects.count(), 1000)
