# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

'''
Nesse formato, o JSON servido como respota sempre irá retornar o password, 
o que pode ser um risco de segurança ou simplesmentes desnessário na maior parte do tempo
'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_active']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
