from rest_framework import serializers
from .models import Usuario, Mensaje, Ticket

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
