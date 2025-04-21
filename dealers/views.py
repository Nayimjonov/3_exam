from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.paginations import DealerPagination
from .models import Dealer
from .serializers import DealerSerializer, DealerCreateSerializer


class DealerListCreateView(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    pagination_class = DealerPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DealerCreateSerializer
        return DealerSerializer


class DealerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer










