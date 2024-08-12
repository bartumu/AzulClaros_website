
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from FuncDashboard.models import *
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError
import re

class FormRegistarCliente(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'insira o seu Nome Completo',
            'id':'nome',
            'class': 'single-input' }), required=True)
    numero = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Insira o Número de Telefone',
            'class': 'single-input'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder': 'Insira o Endereço de Email',
            'class': 'single-input'}), required=True)

    class Meta:
        model = Cliente
        fields = ['nome', 'numero', 'genero', 'email']

    def __init__(self, *args, **kwargs):
        super(FormRegistarCliente, self).__init__(*args, **kwargs)
        self.fields['numero'].label = 'Telefone'
        self.fields['nome'].label = 'Nome Completo'

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        
        # Verifica se o número está no formato correto
        if not re.match(r'^9\d{8}$', numero):
            raise ValidationError('O numero deve começar com 9 e ter 9 dígitos no total.')

        return numero

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email and Cliente.objects.filter(email=email).exists():
            # Recupera o cliente existente e define self.instance para evitar uma nova inserção
            cliente = Cliente.objects.get(email=email)
            self.instance = cliente

        return cleaned_data
 

    def save(self, commit=True):
        #telefone = self.cleaned_data.get('numero')
        #if not re.match(r'^9\d{8}$', telefone):
        #    raise ValidationError("Por favor, insira um número de telemóvel válido com 9 dígitos, começando com 9.")
        # Usa a instância atual se um cliente existente foi definido
        return super().save(commit=commit)

class FormFazerReserva(forms.ModelForm):
    data_entrada = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'single-input'}),
        input_formats=['%Y-%m-%d'], required=True  # Opcional: define o formato de entrada aceitável
    )
    class Meta:
        model = Reserva
        fields = ['data_entrada']

    def __init__(self, *args, **kwargs):
        super(FormFazerReserva, self).__init__(*args, **kwargs)
        self.fields['data_entrada'].label = 'Data de Entrada na Lavandaria'
        

class FormReservaServico(forms.ModelForm):
    servicos = forms.ModelMultipleChoiceField(queryset=Servico.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    qtd = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Insira a Quantidade','class': 'single-input'}), required=True)
    class Meta:
        model = ServicosReservado
        fields = ['qtd']
        
    
class FeedbackForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
            'placeholder': 'Insira o Email',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Insira o Email'",
            'required': True,
        })) 
    comentario = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder': 'Deixe seu comentário',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Deixe seu comentário'",
            'required': True,
        }))
    
    
    class Meta:
        model = Feedback
        fields = ['avaliacao', 'comentario']
        labels = {
            'avaliacao': 'Avaliação (1 a 5)',
            'comentario': 'Comentário'
        }

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})





 #username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'utilizador'}))
    """ nome = forms.CharField(widget=forms.TextInput(attrs={
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
     """