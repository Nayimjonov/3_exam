from rest_framework import generics
from core.paginations import CarPagination
from .models import Car
from .serializers import CarSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    pagination_class = CarPagination
    serializer_class = CarSerializer

