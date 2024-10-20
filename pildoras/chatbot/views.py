from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Mensaje, Ticket
from .serializers import UsuarioSerializer, MensajeSerializer, TicketSerializer
import requests  # Para enviar datos a Magic Loops
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.shortcuts import render

@method_decorator(csrf_exempt, name='dispatch')
class MensajeView(APIView):
    def post(self, request):
        mensaje = request.data.get('contenido')
        usuario = request.data.get('usuario')

        # Simulación de consulta a Magic Loops (puede adaptarse según la API real)
        response = requests.post(
            "https://magicloops.dev/webhook",
            json={'mensaje': mensaje, 'usuario': usuario}
        )

        if response.status_code == 200:
            respuesta = response.json().get('respuesta', 'No se encontró una respuesta.')
            return Response({'respuesta': respuesta}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Error al conectar con Magic Loops.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def dashboard_view(request):
    return render(request, 'pages/index.html')