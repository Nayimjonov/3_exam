from rest_framework import generics
from .models import Dealer
from .serializers import DealerSerializer


class DealerListCreateVie(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
