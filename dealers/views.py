from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.paginations import DealerPagination
from .models import Dealer
from .serializers import DealerSerializer, DealerCreateSerializer, ListingSerializer
from listings.models import Listing


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


class DealerListingView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        dealer_id = self.kwargs['dealer_id']
        dealer = Dealer.objects.get(id=dealer_id)
        return Listing.objects.filter(dealer=dealer)









