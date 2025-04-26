from  rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Listing
from .serializers import ListingSerializer, ListingDetailSerializer
from core.paginations import ListingPagination


class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = ListingPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny]


class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()

    def get_serializer_class(self):
        if self.request.method == ['PUT', 'PATCH']:
            return ListingSerializer
        return ListingDetailSerializer



