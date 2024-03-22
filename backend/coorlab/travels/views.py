from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import Viagem
from .serializers import ViagemSerializer, GroupedViagensSerializer
from django.views.decorators.csrf import csrf_exempt

import json
import os

# Create your views here.
@csrf_exempt
def get_data_json(request):
    file_path = "C:/Users/davih/OneDrive/Área de Trabalho/coorlab/coorlab/backend/coorlab/data/data.json"
    try:
        # Abrindo o arquivo data.json e lendo seu conteúdo
        with open(file_path) as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, retorne um erro 404
        return JsonResponse({'error': 'Arquivo data.json não encontrado'}, status=404)
    
class ViagemList(generics.ListAPIView):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

class ViagemMaisRapidaEConfortavel(views.APIView):
    def get(self, request, *args, **kwargs):
        viagem_mais_rapida = Viagem.objects.order_by("duracao").first()
        viagem_mais_confortavel = Viagem.objects.order_by("-preco_conforto").first()
        serializer = ViagemSerializer([viagem_mais_rapida, viagem_mais_confortavel], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ViagemPorDestinoData(generics.ListAPIView):
    serializer_class = ViagemSerializer

    def get_queryset(self):
        destino = self.request.query_params.get("destino", None)
        data_viagem = self.request.query_params.get("data_viagem", None)
        queryset = Viagem.objects.all()
        if destino:
            queryset = queryset.filter(cidade_destino=destino)
        if data_viagem:
            queryset = queryset.filter(Q(data_ida=data_viagem) | Q(data_volta=data_viagem))
        return queryset
    
class ViagemCreateView(generics.CreateAPIView):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_header(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
