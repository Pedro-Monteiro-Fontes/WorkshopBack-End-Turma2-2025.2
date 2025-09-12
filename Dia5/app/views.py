import requests
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Endereco
from .forms import EnderecoForm
from .serializers import EnderecoSerializer
from django.views.generic import ListView, CreateView, DeleteView




class AdicionarEnderecoView(CreateView):
    model = Endereco
    template_name = "app/adicionar_endereco.html"
    form_class = EnderecoForm
    success_url = reverse_lazy('listar_enderecos')

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        # Faz a requisição para a API ViaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                # Cria o objeto endereco com os dados retornados pela API
                Endereco.objects.create(
                    cep=cep,
                    rua=dados.get('logradouro', ''),
                    bairro=dados.get('bairro', ''),
                    cidade=dados.get('localidade', ''),
                    estado=dados.get('uf', '')
                )
                return super().form_valid(form)
            else:
                form.add_error('cep', 'CEP inválido.')
        else:
            form.add_error('cep', 'Erro ao buscar o CEP. Tente novamente.')
        return super().form_invalid(form)

class ListarEnderecosView(ListView):
    model = Endereco
    template_name = 'app/listar_endereco.html'
    context_object_name = 'enderecos'

class ExcluirEnderecoView(DeleteView):
    model = Endereco
    template_name = 'app/confirmar_exclusao.html'
    success_url = reverse_lazy('listar_enderecos')

class ViaCepAPIView(APIView):
    
    def get(self, request):
        endereco = endereco.objects.all()
        serializer = EnderecoSerializer(endereco, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        cep=request.data.get('cep')
        if not cep:
            return Response({'erro': 'O compo CEP é Obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
        Response = request.get(f'https:viacep.com.br/ws/{cep}/json')
        if Response.status_code == 200:
            dados = Response.json()
            if 'erro' not in dados:
                endereco_obj = Endereco.objcts.create(
                    cep=cep,
                    rua=dados.get('logradouro',''),
                    bairro=dados.get('bairro',''),
                    cidade=dados.get('localidade',''),
                    estado=dados.get('uf','')
                )
                serializer = EnderecoSerializer(endereco_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'erro': 'CEP inválidado'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'erro': 'Erro ao buscar o CEP.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


