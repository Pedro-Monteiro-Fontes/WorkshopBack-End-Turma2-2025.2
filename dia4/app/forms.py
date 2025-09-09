from django.forms import forms
from Projeto_CEP.app.models import endeco

class Enderecoform(forms.Modelform):
  class Meta:
    model = endeco
    fields = ['cep']
    labels = {'cep':'CEP'}
    widgets = {'cep': forms.TextInput(attrs={'classs': 'form-control', 'placeholder': 'Digite o CEP'})}