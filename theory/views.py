from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer


class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
