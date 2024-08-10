from django.test import TestCase
from FuncDashboard.models import Funcionario, Servico, Cliente, Reserva, ServicosReservado, MetodoPagamento, Pagamentos
from UserAutenticacao.models import Usuario 

from django.contrib.auth import get_user_model

Usuario = get_user_model()

class FuncionarioModelTest(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(username='test',email='testuser@example.com', password='testpass')
        self.funcionario = Funcionario.objects.create(
            nome='João Silva',
            endereco='Rua Principal',
            numero='912345678',
            genero='M',
            usuario=self.usuario
        )

    def test_funcionario_creation(self):
        self.assertEqual(self.funcionario.nome, 'João Silva')
        self.assertEqual(self.funcionario.endereco, 'Rua Principal')
        self.assertEqual(self.funcionario.numero, '912345678')
        self.assertEqual(self.funcionario.genero, 'M')
        self.assertEqual(self.funcionario.usuario.email, 'testuser@example.com')
        self.assertFalse(bool(self.funcionario.img))
        

class ServicoModelTest(TestCase):

    def setUp(self):
        self.servico = Servico.objects.create(
            nome='Lavagem Simples',
            descricao='Lavagem básica de roupas.',
            preco=10.00
        )

    def test_servico_creation(self):
        self.assertEqual(self.servico.nome, 'Lavagem Simples')
        self.assertEqual(self.servico.descricao, 'Lavagem básica de roupas.')
        self.assertEqual(self.servico.preco, 10.00)
        self.assertFalse(bool(self.servico.img))

class ClienteModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Maria Oliveira',
            endereco='Rua Secundária',
            email='maria@example.com',
            numero='923456789',
            genero='F'
        )

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nome, 'Maria Oliveira')
        self.assertEqual(self.cliente.endereco, 'Rua Secundária')
        self.assertEqual(self.cliente.email, 'maria@example.com')
        self.assertEqual(self.cliente.numero, '923456789')
        self.assertEqual(self.cliente.genero, 'F')

class ReservaModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Carlos Alberto',
            endereco='Rua Tercenária',
            email='carlos@example.com',
            numero='934567890',
            genero='M'
        )
        self.reserva = Reserva.objects.create(
            cliente=self.cliente,
            estado=0,
            data_entrada='2024-08-01',
            data_saida='2024-08-03'
        )

    def test_reserva_creation(self):
        self.assertEqual(self.reserva.cliente, self.cliente)
        self.assertEqual(self.reserva.estado, 0)
        self.assertEqual(self.reserva.data_entrada, '2024-08-01')
        self.assertEqual(self.reserva.data_saida, '2024-08-03')
        self.assertIsNotNone(self.reserva.codigo_reserva)


class ServicosReservadoModelTest(TestCase):

    def setUp(self):
        self.servico = Servico.objects.create(
            nome='Lavagem Completa',
            descricao='Lavagem completa de roupas.',
            preco=20.00
        )
        self.cliente = Cliente.objects.create(
            nome='Carlos Alberto',
            endereco='Rua Tercenária',
            email='carlos@example.com',
            numero='934567890',
            genero='M'
        )
        self.reserva = Reserva.objects.create(
            cliente=self.cliente,
            estado=0,
            data_entrada='2024-08-01',
            data_saida='2024-08-03'
        )
        self.servicos_reservado = ServicosReservado.objects.create(
            reserva=self.reserva,
            servico=self.servico,
            qtd=2,
            subtotal=40.00
        )

    def test_servicos_reservado_creation(self):
        self.assertEqual(self.servicos_reservado.reserva, self.reserva)
        self.assertEqual(self.servicos_reservado.servico, self.servico)
        self.assertEqual(self.servicos_reservado.qtd, 2)
        self.assertEqual(self.servicos_reservado.subtotal, 40.00)

class MetodoPagamentoModelTest(TestCase):

    def setUp(self):
        self.metodo_pagamento = MetodoPagamento.objects.create(metodo='Dinheiro')

    def test_metodo_pagamento_creation(self):
        self.assertEqual(self.metodo_pagamento.metodo, 'Dinheiro')

class PagamentosModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Carlos Alberto',
            endereco='Rua Tercenária',
            email='carlos@example.com',
            numero='934567890',
            genero='M'
        )
        self.reserva = Reserva.objects.create(
            cliente=self.cliente,
            estado=0,
            data_entrada='2024-08-01',
            data_saida='2024-08-03'
        )
        self.metodo_pagamento = MetodoPagamento.objects.create(metodo='Cartão de Crédito')
        self.pagamento = Pagamentos.objects.create(
            valor=50.00,
            metodoPagamento=self.metodo_pagamento,
            reserva=self.reserva
        )

    def test_pagamentos_creation(self):
        self.assertEqual(self.pagamento.valor, 50.00)
        self.assertEqual(self.pagamento.metodoPagamento, self.metodo_pagamento)
        self.assertEqual(self.pagamento.reserva, self.reserva)
        self.assertIsNotNone(self.pagamento.dataPagamento)

