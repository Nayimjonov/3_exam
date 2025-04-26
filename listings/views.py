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


class ListingImagesListView(generics.ListAPIView):
    serializer_class = ListingImagesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return ListingImage.objects.filter(listing_id=listing_id)


class ListingImagesCreateView(generics.CreateAPIView):
    serializer_class = ListingImagesSerializer
    permission_classes = [IsListingOwner]

    def perform_create(self, serializer):
        listing_id = self.kwargs.get('listing_id')
        listing = get_object_or_404(Listing, id=listing_id)
        serializer.save(listing=listing)


class ListingImageDeleteView(generics.DestroyAPIView):
    serializer_class = ListingImagesSerializer
    permission_classes = [IsListingOwner]

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return ListingImage.objects.filter(listing_id=listing_id)


class ListingPriceHistoryView(generics.ListAPIView):
    serializer_class = PriceHistorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return PriceHistory.objects.filter(listing_id=listing_id).order_by('-created_at')


class FeaturedListingsView(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ListingPagination  # Assuming you have this defined

    def get_queryset(self):
        return Listing.objects.filter(
            is_featured=True,
            is_active=True,
            expires_at__gt=timezone.now()
        ).order_by('-created_at')


class MyListingsView(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListingPagination

    def get_queryset(self):
        return Listing.objects.filter(seller=self.request.user).order_by('-created_at')
