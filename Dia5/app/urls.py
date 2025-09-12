from django.urls import path 
from .views import ListarEnderecosView, ViaCepAPIView, AdicionarEnderecoView, ExcluirEnderecoView


urlpatterns = [
    path('', ListarEnderecosView.as_view(), name='listar_enderecos'),  # Lista de endereços
    path('api/viacep/', ViaCepAPIView.as_view(), name='viacep_api'),
    path('enderecos/novo/', AdicionarEnderecoView.as_view(), name='adicionar_endereco'),  # Criar novo endereço
    path('excluir/<int:pk>/', ExcluirEnderecoView.as_view(), name='excluir_endereco'),  # Excluir endereço
]