from django.shortcuts import render
import requests
# Create your views here.
def home(request):
  return render(request, 'home.html')

def endereco(request):
  cep = request.GET.get('cep')
  endereco =None

  if cep:
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
      endereco = response.json()
      if 'erro' in endereco:
        endereco =None

  return render(request,'endereco.html', {'endereco': endereco} )