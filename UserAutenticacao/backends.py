# backends.py

from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from django.db.models import Q
from UserAutenticacao.models import Usuario  # Importar o modelo de usuário personalizado

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Procura pelo usuário usando o email ou username
            user = Usuario.objects.get(Q(username=username) | Q(email=username))
        except:
            return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except:
            return None
