from rest_framework import generics
from core.paginations import CarPagination
from .models import Car
from .serializers import CarListSerializer, CarCreateSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    pagination_class = CarPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CarCreateSerializer
        return CarListSerializer