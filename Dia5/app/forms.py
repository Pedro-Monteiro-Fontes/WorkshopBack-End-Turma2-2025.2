from django import forms
from .models import Endereco   # Model sempre com inicial maiúscula

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep']  # Só o campo CEP por enquanto
        labels = {'cep': 'CEP'}
        widgets = {
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o CEP'
            })
        }
