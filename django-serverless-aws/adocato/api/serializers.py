from rest_framework import serializers
from .models import Usuario, Adocao, Raca, Gato

class RacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = ['nome']

class GatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gato
        fields = ['nome', 'raca', 'idade', 'peso', 'data_cadastro', 'foto']
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'data_cadastro', 'cpf', 'endereco']

class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = ['gato', 'adotante', 'data_criacao', 'data_analise', 'status_opts']