from  rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from core.paginations import ListingPagination


class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = ListingPagination

