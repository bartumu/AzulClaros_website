from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from UserAutenticacao.models import Usuario
from django.core.exceptions import ValidationError


class FormRegistarUser(UserCreationForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'utilizador'}))
    username = forms.CharField(label="Nome de Utilizador", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'userpassword'}))
    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirmpassword'})) 
    class Meta:
        model = Usuario
        fields = ['username','email']

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['email', 'username','is_superuser']  
        labels = {
            'email': 'Endereço de E-mail',
            'username': 'Nome de Usuário',  
            'is_superuser': 'Administrador',
        }
        help_texts = {
            'email': 'Digite um endereço de e-mail válido.',
        }
    
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        self.fields['is_superuser'] = forms.BooleanField(required=False, label='Administrador')  


class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ['email', 'username','is_superuser']  
        labels = {
            'email': 'Endereço de E-mail',
            'username': 'Nome de Usuário',  
            'is_superuser': 'Administrador',
        }
        help_texts = {
            'email': 'Digite um endereço de e-mail válido.',
        }
    
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        self.fields['is_superuser'] = forms.BooleanField(required=False, label='Administrador')  


class RecuperarSenhaForm(forms.ModelForm):
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

    class Meta:
        model = Usuario
        fields = ['password']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RecuperarSenhaForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if field_name == 'img':
                field.widget.attrs.update({'class': 'dropfy','id':'input-file-now-custom-1'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
        
        if user:
            self.fields['email'].initial = user.email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        
        if password and password != password_confirmation:
            raise ValidationError("As senhas não correspondem.")

        return cleaned_data

    def save(self, commit=True):
        usuario = super(RecuperarSenhaForm, self).save(commit=False)
        
        usuario.email = self.cleaned_data['email']

        if self.cleaned_data['password']:
            usuario.set_password(self.cleaned_data['password'])

        if commit:
            usuario.save()

        return usuario
