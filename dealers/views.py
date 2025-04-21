from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from listings.models import Listing
from core.paginations import DealerPagination, ResultPagination
from reviews.models import Review

from .models import Dealer
from .serializers import DealerSerializer, DealerCreateSerializer, ListingSerializer, DealerReviewSerializer



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


#dealer/<pk>/listings/
class DealerListingsView(generics.ListAPIView):
    serializer_class = ListingSerializer
    pagination_class = DealerPagination

    def get_queryset(self):
        dealer_id = self.kwargs['dealer_id']
        try:
            dealer = Dealer.objects.get(id=dealer_id)
        except Dealer.DoesNotExist:
            raise NotFound(detail="Dealer not found")

        return Listing.objects.filter(seller=dealer.user)


#dealer/<pk>/reviews/
class DealerReviewList(generics.ListCreateAPIView):
    serializer_class = DealerReviewSerializer
    pagination_class = ResultPagination



    def get_dealer(self):
        return get_object_or_404(Dealer, pk=self.kwargs['dealer_pk'])

    def get_queryset(self):
        dealer = self.get_dealer()
        return Review.objects.filter(reviewed_user=dealer.user).order_by('-created_at')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['dealer'] = self.get_dealer()
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

        result_serializer = self.get_serializer(review)
        return Response(result_serializer.data, status=201)





