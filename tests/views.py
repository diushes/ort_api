from .models import Test
from rest_framework import generics
from .serializers import TestSerializer


class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
