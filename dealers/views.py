from rest_framework import generics
from core.paginations import DealerPagination
from .models import Dealer
from .serializers import DealerSerializer


class DealerListCreateVie(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    pagination_class = DealerPagination
