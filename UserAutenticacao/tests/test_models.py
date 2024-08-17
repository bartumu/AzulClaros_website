from django.test import TestCase
from django.core.exceptions import ValidationError
from UserAutenticacao.models import Usuario

class UsuarioModelTest(TestCase):

    def test_criacao_usuario_valido(self):
        usuario = Usuario.objects.create_user(email='teste@exemplo.com', username='testeuser', password='senha123')
        self.assertEqual(usuario.email, 'teste@exemplo.com')
        self.assertEqual(usuario.username, 'testeuser')
    
    def test_criacao_usuario_email_duplicado(self):
        Usuario.objects.create_user(email='duplicado@exemplo.com', username='user1', password='senha123')
        with self.assertRaises(ValidationError):
            Usuario.objects.create_user(email='duplicado@exemplo.com', username='user2', password='senha456')

    def test_criacao_usuario_sem_username(self):
        with self.assertRaises(ValidationError):
            Usuario.objects.create_user(email='nousername@exemplo.com', username='', password='senha123')

    def test_metodo_str_retorna_email(self):
        usuario = Usuario.objects.create_user(email='teste@exemplo.com', username='testeuser', password='senha123')
        self.assertEqual(str(usuario), 'teste@exemplo.com')
