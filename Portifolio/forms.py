
from django import forms
from .models import *




class CliForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar o campo `user` para mostrar apenas usuários do tipo "funcionário"
        self.fields['usuario'].queryset = Usuario.objects.filter(user_tipo='cliente')
