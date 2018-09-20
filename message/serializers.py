from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'text', 'date', 'status']
