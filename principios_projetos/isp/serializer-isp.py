# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

'''
Nessa refatoração, o Serializar anterior é dividido em dois, de forma que um é responsável pela criação do usuário 
e outro pela manipulação, sem incorporar o password, por exemplo, na resposta a requisição
'''

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserCreationSerializer, self).create(validated_data)
    
    #Se precisar permitir troca do password, implemente o método update e se for o caso, troque o nome da classe

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
