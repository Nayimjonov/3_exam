from  rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Listing
from .serializers import ListingSerializer, ListingDetailSerializer, ImageSerializer, PriceHistorySerializer
from .permissions import IsListingOwner
from core.paginations import ListingPagination
from images.models import Image
from price_histories.models import PriceHistory



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


class ListingImagesView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return Image.objects.filter(listing_id=listing_id).order_by('order')

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsListingOwner()]
        return [AllowAny()]

    def perform_create(self, serializer):
        listing_id = self.kwargs.get('listing_id')
        listing = get_object_or_404(Listing, id=listing_id)
        serializer.save(listing=listing)


class ListingImageDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsListingOwner]

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return Image.objects.filter(listing_id=listing_id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_primary:
            next_image = Image.objects.filter(
                listing_id=self.kwargs.get('listing_id')
            ).exclude(id=instance.id).order_by('order').first()

            if next_image:
                next_image.is_primary = True
                next_image.save()

                instance.listing.primary_image = next_image.image
                instance.listing.save(update_fields=['primary_image'])
            else:
                instance.listing.primary_image = None
                instance.listing.save(update_fields=['primary_image'])

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListingPriceHistoryView(generics.ListAPIView):
    serializer_class = PriceHistorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return PriceHistory.objects.filter(listing_id=listing_id).order_by('-created_at')


class FeaturedListingsView(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]
    pagination_class = ListingPagination

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
