from django.test import TestCase
from FuncDashboard.forms import *
from Portifolio.forms import *
from django.urls import reverse

#Testes de Validação de Formulário

class FormCadFuncionarioTest(TestCase):
    def test_form_valid(self):
        form_data = {
            'nome': 'Test User',
            'endereco': 'Test Address',
            'numero': '912345678',
            'genero': 'M'
        }
        form = FormCadFuncionario(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            'nome': '',
            'endereco': 'Test Address',
            'numero': '123',  # Número inválido
            'genero': 'M'
        }
        form = FormCadFuncionario(data=form_data)
        self.assertFalse(form.is_valid())

#Testes de Campos Obrigatórios
class FormRegistarClienteTest(TestCase):
    def test_required_fields(self):
        form_data = {
            'nome': '',
            'numero': '',
            'genero': '',
            'email': ''
        }
        form = FormRegistarCliente(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('numero', form.errors)
        self.assertIn('email', form.errors)


#Testes de Integração
""" 
class FormRegistarClienteIntegrationTest(TestCase):
    def test_form_submission(self):
        form_data = {
            'nome': 'Cliente Teste',
            'numero': '912345678',
            'genero': 'M',
            'email': 'cliente@teste.com'
        }
        response = self.client.post(reverse('reservaAdd'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Verifica redirecionamento após sucesso
        self.assertTrue(Cliente.objects.filter(email='cliente@teste.com').exists())


#Testes de Visualização de Formulário

class FormVisualizationTest(TestCase):
    def test_form_rendering(self):
        response = self.client.get(reverse('perfil'))
        self.assertContains(response, 'placeholder="Nome"')
        self.assertContains(response, 'class="form-control"') """


#Teste de Comportamento personalizado

class FormRegistarClienteCustomTest(TestCase):
    def test_clean_method(self):
        existing_cliente = Cliente.objects.create(nome='Test', email='test@example.com', numero='912345678')
        form_data = {
            'nome': 'Test',
            'numero': '912345678',
            'genero': 'M',
            'email': 'test@example.com'
        }
        form = FormRegistarCliente(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.instance, existing_cliente)  # Verifica se o cliente existente foi usado


#TEste de Relaccionamento entre modelos
class ServicosReservadoFormTest(TestCase):
    def test_servicos_reservado_creation(self):
        cliente = Cliente.objects.create(nome='Cliente Teste', email='cliente@teste.com', numero='912345678')
        reserva = Reserva.objects.create(cliente=cliente)
        servico = Servico.objects.create(nome='Lavagem Simples', preco=100.0)
        
        form_data = {
            'reserva': reserva.id,
            'servico': servico.id,
            'qtd': 2
        }
        form = FormReservaServico(data=form_data)
        self.assertTrue(form.is_valid())