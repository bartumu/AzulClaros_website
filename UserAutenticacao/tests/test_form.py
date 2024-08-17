from django.test import TestCase
from UserAutenticacao.forms import FormRegistarUser, UsuarioChangeForm
from UserAutenticacao.models import Usuario

class FormRegistarUserTest(TestCase):

    def test_form_valido_com_dados_corretos(self):
        form_data = {
            'username': 'testeuser',
            'email': 'teste@exemplo.com',
            'password1': 'senha123',
            'password2': 'senha123',
        }
        form = FormRegistarUser(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalido_senhas_diferentes(self):
        form_data = {
            'username': 'testeuser',
            'email': 'teste@exemplo.com',
            'password1': 'senha123',
            'password2': 'senha456',
        }
        form = FormRegistarUser(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_form_invalido_email_ja_existente(self):
        Usuario.objects.create_user(email='teste@exemplo.com', username='testeuser', password='senha123')
        form_data = {
            'username': 'novo_user',
            'email': 'teste@exemplo.com',
            'password1': 'senha123',
            'password2': 'senha123',
        }
        form = FormRegistarUser(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class UsuarioChangeFormTest(TestCase):

    def test_alteracao_email_e_username(self):
        usuario = Usuario.objects.create_user(email='original@exemplo.com', username='useroriginal', password='senha123')
        form_data = {
            'email': 'novoemail@exemplo.com',
            'username': 'usernovo',
        }
        form = UsuarioChangeForm(data=form_data, instance=usuario)
        self.assertTrue(form.is_valid())
        form.save()
        usuario.refresh_from_db()
        self.assertEqual(usuario.email, 'novoemail@exemplo.com')
        self.assertEqual(usuario.username, 'usernovo')

    def test_alteracao_email_duplicado(self):
        usuario1 = Usuario.objects.create_user(email='user1@exemplo.com', username='user1', password='senha123')
        Usuario.objects.create_user(email='user2@exemplo.com', username='user2', password='senha123')
        form_data = {
            'email': 'user2@exemplo.com',
            'username': 'user1',
        }
        form = UsuarioChangeForm(data=form_data, instance=usuario1)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)