from rest_framework import serializers
from .models import Viagem

class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields = "__all__"

class GroupedViagensSerializer(serializers.Serializer):
    main = serializers.ListSerializer(child=ViagemSerializer())
    others = serializers.ListSerializer(child=ViagemSerializer())

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Viagem  # Importe seu modelo Viagem
from .serializers import ViagemSerializer  # Importe seu ViagemSerializer

class ViagemFiltradaAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Recupere destino e data dos dados da requisição
        destino = request.data.get('destino')
        data = request.data.get('data')

        # Filtre com base em destino e data (se fornecidos)
        if destino and data:
            viagens = Viagem.objects.filter(destino=destino, data=data)
        elif destino:
            viagens = Viagem.objects.filter(destino=destino)
        elif data:
            viagens = Viagem.objects.filter(data=data)
        else:
            viagens = Viagem.objects.all()  # Todas as viagens se nenhum filtro

        # Ordene por preço (crescente) e selecione a mais barata e a mais cara
        mais_barata = viagens.order_by('preco_conforto').first()
        mais_cara = viagens.order_by('-preco_conforto').first()

        # Serializa os resultados filtrados
        serializer = ViagemSerializer([mais_barata, mais_cara], many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
