from rest_framework import serializers
from django.contrib.auth.models import User
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
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['cpf'], email=validated_data['email'])
        usuario = Usuario.objects.create(user=user, **validated_data)
        return usuario

class AdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = ['gato', 'adotante', 'data_criacao', 'data_analise', 'status_opts']