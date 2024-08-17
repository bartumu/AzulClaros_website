from django.test import TestCase
from FuncDashboard.models import *

class CadastroClienteTest(TestCase):
    def test_cliente_cadastro(self):
        cliente = Cliente.objects.create(
            nome="João Silva",
            numero="923456789",
            email="joao.silva@example.com"
        )
        self.assertEqual(cliente.nome, "João Silva")
        self.assertEqual(cliente.numero, "923456789")
        self.assertEqual(cliente.email, "joao.silva@example.com")
        self.assertTrue(Cliente.objects.filter(email="joao.silva@example.com").exists())


        
class GestaoClienteTest(TestCase):
    def test_cliente_edicao(self):
        cliente = Cliente.objects.create(
            nome="João Silva",
            numero="923456789",
            email="joao.silva@example.com"
        )
        cliente.nome = "João Souza"
        cliente.save()
        
        self.assertEqual(cliente.nome, "João Souza")

    def test_visualizar_historico_pedidos(self):
        cliente = Cliente.objects.create(
            nome="João Silva",
            numero="923456789",
            email="joao.silva@example.com"
        )
        reserva = Reserva.objects.create(
            cliente=cliente,
            data_entrada="2024-08-16"
        )
        self.assertEqual(cliente.reserva_set.count(), 1)


class GestaoReservaTest(TestCase):
    def test_registro_nova_reserva(self):
        cliente = Cliente.objects.create(
            nome="Maria Santos",
            numero="923456789",
            email="maria.santos@example.com"
        )
        reserva = Reserva.objects.create(
            cliente=cliente,
            data_entrada="2024-08-16",
            estado=0
        )
        self.assertEqual(reserva.estado, 0)

    def test_atualizar_status_reserva(self):
        reserva = Reserva.objects.create(
            cliente=Cliente.objects.create(nome="Maria Santos", numero="923456789", email="maria.santos@example.com"),
            data_entrada="2024-08-16",
            estado=0
        )
        reserva.estado = 1
        reserva.save()

        self.assertEqual(reserva.estado, 1)

class GestaoPagamentoTest(TestCase):
    def test_processamento_pagamento(self):
        cliente = Cliente.objects.create(
            nome="Pedro Oliveira",
            numero="923456789",
            email="pedro.oliveira@example.com"
        )
        reserva = Reserva.objects.create(
            cliente=cliente,
            data_entrada="2024-08-16"
        )
        pagamento = Pagamentos.objects.create(
            reserva=reserva,
            metodoPagamento=MetodoPagamento.objects.create(metodo="Cartão"),
            valor=1000.00
        )
        self.assertEqual(pagamento.metodoPagamento.metodo, "Cartão")
        self.assertEqual(pagamento.valor, 1000.00)

class ManutencaoRegistrosTest(TestCase):
    def test_manutencao_registros(self):
        cliente = Cliente.objects.create(
            nome="Carlos Ferreira",
            numero="923456789",
            email="carlos.ferreira@example.com"
        )
        reserva = Reserva.objects.create(
            cliente=cliente,
            data_entrada="2024-08-16"
        )
        self.assertTrue(Reserva.objects.filter(cliente=cliente).exists())
        self.assertEqual(Reserva.objects.count(), 1)


from django.core import mail

class SistemaNotificacoesTest(TestCase):
    def test_notificacao_cliente(self):
        cliente = Cliente.objects.create(
            nome="Ana Costa",
            numero="923456789",
            email="ana.costa@example.com"
        )
        reserva = Reserva.objects.create(
            cliente=cliente,
            data_entrada="2024-08-16"
        )
        mail.send_mail(
            'Status do Pedido',
            'Seu pedido foi0',
            'from@example.com',
            [cliente.email]
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Status do Pedido')


from django.contrib.auth.models import Group

class ControleAcessoSegurancaTest(TestCase):
    def test_acesso_funcionario(self):
        user = Usuario.objects.create_user(
            email="funcionario@example.com",
            password="testpassword",
            username="funcionario"
        )
        user.is_superuser = False
        self.assertFalse(user.is_superuser)

    def test_acesso_admin(self):
        admin = Usuario.objects.create_user(
            email="admin@example.com",
            password="adminpassword",
            username="admin"
        )
        admin.is_staff = True
        admin.save()
        self.assertTrue(admin.is_staff)
