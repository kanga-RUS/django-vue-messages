from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MessagesListView(generics.ListAPIView):
    """
    This class return new messages (read status = False) from DB
    """
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.filter(status=False).order_by('-date')
        id_message = self.request.query_params.get('last_id', None)
        if id_message is not None:
            queryset = queryset.filter(id__gt=id_message)
        return queryset


class MessageUpdateView(generics.RetrieveUpdateAPIView):
    """
    Class change status of message
    """
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.filter(status=False)
        id_message = self.request.query_params.get('id', None)
        if id_message is not None:
            queryset = get_object_or_404(Message, id=id_message)
        return queryset

    def get_object(self):
        obj = self.get_queryset()
        return obj
