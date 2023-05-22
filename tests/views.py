from .models import Test
from rest_framework import generics
from .serializers import TestSerializer


class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestsByCategoryListView(generics.ListAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']  # Assuming category_id is passed as a URL parameter
        return Test.objects.filter(category=category_id)