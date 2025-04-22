from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Make, Model, BodyType, Feature
from .serializers import MakeSerializer, ModelSerializer, BodyTypeSerializer, FeatureSerializer
from core.paginations import MakePagination, BodyTypePagination, FeaturePagination


class MakeListView(generics.ListAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    pagination_class = MakePagination
    permission_classes = [AllowAny]


class ModelListByMakeView(generics.ListAPIView):
    serializer_class = ModelSerializer
    pagination_class = MakePagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        make_id = self.kwargs.get('make_id')
        return Model.objects.filter(make_id=make_id)


class BodyTypeListView(generics.ListAPIView):
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeSerializer
    pagination_class = BodyTypePagination
    permission_classes = [AllowAny]


class FeatureListView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    pagination_class = FeaturePagination
    permission_classes = [AllowAny]

