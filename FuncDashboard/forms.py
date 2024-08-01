from django import forms
from .models import Funcionario, Usuario
from .models import *

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
    """ genero = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={
            'class': 'form-control'
        })) """
    """ img = forms.ImageField(widget=forms.FileInput(attrs={
            'id': 'input-file-now-custom-1',
            'class': 'dropify',
        })) """
    
    class Meta:
        model = Funcionario
        fields = ['nome','endereco','numero','genero']

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
