from django import forms
from .models import Funcionario, Usuario
from .models import *
from django.core.exceptions import ValidationError
import re

class FormCadFuncionario(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Nome',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Nome'",
            'required': True,
            'class': 'form-control'
        }))
    numero = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Numero de Tel',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Número de Tel'",
            'required': True,
            'class': 'form-control'
        }))
    endereco = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Endereço',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Endereço'",
            'required': True,
            'class': 'form-control'
        }))
    
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        
        # Verifica se o número está no formato correto
        if not re.match(r'^9\d{8}$', numero):
            raise ValidationError('O numero deve começar com 9 e ter 9 dígitos no total.')

        return numero
    
    class Meta:
        model = Funcionario
        fields = ['nome','endereco','numero','genero']

class FuncionarioPerfilForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        required=False,
        help_text="Deixe em branco se não quiser alterar."
    )
    password_confirm = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput,
        required=False,
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput
    )
    username = forms.CharField(
        label="Nome de Usuário",
        required=True,
        widget=forms.TextInput
    )

    class Meta:
        model = Funcionario
        fields = ['nome', 'endereco', 'numero', 'genero', 'img']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FuncionarioPerfilForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if field_name == 'img':
                field.widget.attrs.update({'class': 'dropfy','id':'input-file-now-custom-1'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
        
        if user:
            self.fields['email'].initial = user.email
            self.fields['username'].initial = user.username


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        
        if password and password != password_confirmation:
            raise ValidationError("As senhas não correspondem.")

        return cleaned_data

    def save(self, commit=True):
        funcionario = super(FuncionarioPerfilForm, self).save(commit=False)
        user = funcionario.usuario
        
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            funcionario.save()

        return funcionario

class FormAtender(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data_saida']

class FormPagamento(forms.ModelForm):
    metodoPagamento = forms.ModelChoiceField(
        queryset=MetodoPagamento.objects.all(),
        widget=forms.Select(attrs={'id': 'metodo-pagamento','class': 'form-control'})
    )
    class Meta:
        model = Pagamentos
        fields=['metodoPagamento']
        """ widgets = {
            'metodoPagamento': forms.ModelChoiceField(queryset=MetodoPagamento.objects.all(),attrs={'id': 'metodo-pagamento'})
        } """


class FuncForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar o campo `user` para mostrar apenas usuários do tipo "funcionário"
        self.fields['usuario'].queryset = Usuario.objects.filter(is_staff=False)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['avaliacao', 'comentario']
        labels = {
            'avaliacao': 'Avaliação (1 a 5)',
            'comentario': 'Comentário'
        }