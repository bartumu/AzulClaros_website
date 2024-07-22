from django import forms
from django.contrib.auth.forms import UserCreationForm
from UserAutenticacao.models import Usuario


class FormRegistarUser(UserCreationForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'utilizador'}))
    username = forms.CharField(label="Nome de Utilizador", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'userpassword'}))
    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirmpassword'})) 
    class Meta:
        model = Usuario
        fields = ['username','email']