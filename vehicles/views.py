from rest_framework import generics
from .models import Make, Model
from .serializers import MakeSerializer, ModelSerializer
from core.paginations import MakePagination


class MakeListView(generics.ListAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    pagination_class = MakePagination


class ModelListByMakeView(generics.ListAPIView):
    serializer_class = ModelSerializer
    pagination_class = MakePagination

    def get_queryset(self):
        make_id = self.kwargs.get('make_id')
        return Model.objects.filter(make_id=make_id)