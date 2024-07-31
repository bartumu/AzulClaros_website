
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class FormRegistarCliente(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Nome',
            'id':'nome',
             'class': 'single-input' }), required=True)
    numero = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Numero de fone',
            'class': 'single-input'}), required=True) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'single-input'}), required=True) 
    class Meta:
        model = Cliente
        fields = ['nome','numero', 'genero', 'email']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email and Cliente.objects.filter(email=email).exists():
            # Recupera o cliente existente e define self.instance para evitar uma nova inserção
            cliente = Cliente.objects.get(email=email)
            self.instance = cliente

        return cleaned_data

    def save(self, commit=True):
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
        

class FormReservaServico(forms.ModelForm):
    servicos = forms.ModelMultipleChoiceField(queryset=Servico.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    qtd = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Quantidade de Cesto','class': 'single-input'}), required=True)
    class Meta:
        model = ServicosReservado
        fields = ['qtd']
        
    


class CliForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar o campo `user` para mostrar apenas usuários do tipo "funcionário"
        self.fields['usuario'].queryset = Usuario.objects.filter(user_tipo='cliente')



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