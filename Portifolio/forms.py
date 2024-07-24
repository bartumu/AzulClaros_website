
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class FormRegistarCliente(UserCreationForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'utilizador'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Nome',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Nome'",
            'required': True,
            'class': 'single-input'
        }))
    numero = PhoneNumberField(region="AO", widget=forms.TextInput(attrs={
            'placeholder': 'Numero de Telemovel',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Numero de telemovel'",
            'required': True,
            'class': 'single-input'
        }))
    genero = forms.ChoiceField(label="Escolha o Genero", choices=[('M', 'Masculino'), ('F', 'Feminino')])
    

class FormFazerPedido(UserCreationForm):
    qtd = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Quantidade de Cestos',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Quantidade de Cestos'",
            'required': True,
            'class': 'single-input'
        }))
    


class CliForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar o campo `user` para mostrar apenas usuários do tipo "funcionário"
        self.fields['usuario'].queryset = Usuario.objects.filter(user_tipo='cliente')
