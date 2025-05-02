from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
from core.paginations import MessagePagination


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessagePagination

