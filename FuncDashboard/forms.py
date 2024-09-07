from django import forms
from .models import Funcionario, Usuario
from .models import *
from django.core.exceptions import ValidationError
import re
from datetime import date
from django.core.validators import RegexValidator

class FormCadFuncionario(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Nome',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Insira o Nome Completo'",
            'required': True,
            'class': 'form-control'
        }), validators=[RegexValidator(
                regex=r'^[A-Za-zÀ-ÿ\s]+$',
                message='O campo deve conter apenas letras e espaços.'
            )])
    numero = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Numero de Tel',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Insira o Número de Telemóvel'",
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
    
    class Meta:
        model = Funcionario
        fields = ['nome','endereco','numero','genero']

    def __init__(self, *args, **kwargs):
        super(FormCadFuncionario, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'genero':
                field.widget.attrs.update({'class': 'form-control'})

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        
        # Verifica se o número está no formato correto
        if not re.match(r'^9\d{8}$', numero):
            raise ValidationError('O numero deve começar com 9 e ter 9 dígitos no total.')

        return numero
    
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
        
    def clean(self):
        cleaned_data = super().clean()
        data_saida = cleaned_data.get('data_saida')
        
        reserva = self.instance
        data_entrada = reserva.data_entrada
        print(data_saida)

        # Verifica se a data é anterior à data de hoje
        if data_entrada and data_saida and data_saida <= data_entrada:
            self.add_error('data_saida', "A data de saída deve ser posterior à data de entrada.")

        return cleaned_data

class FormPagamento(forms.ModelForm):
    metodoPagamento = forms.ModelChoiceField(
        queryset=MetodoPagamento.objects.all(),
        widget=forms.Select(attrs={'id': 'metodo-pagamento','class': 'form-control'})
    )
    class Meta:
        model = Pagamentos
        fields=['metodoPagamento']
        

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

   
class FormRegistarCliente(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'insira o seu Nome Completo',
            'id':'nome',
            'class': 'form-control' }), required=True, validators=[RegexValidator(
                regex=r'^[A-Za-zÀ-ÿ\s]+$',
                message='O campo deve conter apenas letras e espaços.'
            )])
    numero = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Insira o Número de Telefone',
            'class': 'form-control'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder': 'Insira o Endereço de Email',
            'class': 'form-control'}), required=True)

    class Meta:
        model = Cliente
        fields = ['nome', 'numero', 'genero', 'email']

    def __init__(self, *args, **kwargs):
        super(FormRegistarCliente, self).__init__(*args, **kwargs)
        self.fields['numero'].label = 'Telefone'
        self.fields['nome'].label = 'Nome Completo'
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        
        # Verifica se o número está no formato correto
        if not re.match(r'^9\d{8}$', numero):
            self.add_error('numero','O numero deve começar com 9 e ter 9 dígitos no total.')

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
        return super().save(commit=commit)

class FormFazerReserva(forms.ModelForm):
    data_saida = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'], required=True  
    )
    class Meta:
        model = Reserva
        fields = ['data_saida','obs']
        widgets = {  
            'obs': forms.Textarea(attrs={  
                'placeholder': 'Descreva as peças aqui',  
                'rows': 4,  
                'cols': 50,
                'required': 'false',  
            })  
        } 

    def __init__(self, *args, **kwargs):
        super(FormFazerReserva, self).__init__(*args, **kwargs)
        self.fields['data_saida'].label = 'Data De Saída'
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        data_entrada = cleaned_data.get('data_saida')

        # Verifica se a data é anterior à data de hoje
        if data_entrada and data_entrada < date.today():
            self.add_error('data_saida', "A data de Saída não pode ser anterior à data de hoje.")

        return cleaned_data
        

class FormReservaServico(forms.ModelForm):
    servicos = forms.ModelMultipleChoiceField(queryset=Servico.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    qtd = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Insira a Quantidade','class': 'form-control',
            'min': 1,  
            'max': 4 }), required=True)
    class Meta:
        model = ServicosReservado
        fields = ['qtd']
        
  