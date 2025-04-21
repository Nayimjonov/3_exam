from rest_framework import generics
from .models import Make
from .serializers import MakeSerializer


class MakeListView(generics.ListAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer



