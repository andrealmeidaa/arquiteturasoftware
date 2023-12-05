from django.shortcuts import render
from rest_framework import generics
from .models import Raca, Usuario, Gato, Adocao
from .serializers import RacaSerializer, UsuarioSerializer, GatoSerializer, AdocaoSerializer

class RacaListCreate(generics.ListCreateAPIView):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer

class RacaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class GatoListCreate(generics.ListCreateAPIView):
    queryset = Gato.objects.all()
    serializer_class = GatoSerializer

class GatoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gato.objects.all()
    serializer_class = GatoSerializer

class AdocaoListCreate(generics.ListCreateAPIView):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer

class AdocaoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer
