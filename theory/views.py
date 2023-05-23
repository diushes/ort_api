from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from django.http import HttpResponse


def index(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to My Django App</title>
    </head>
    <body>
        <h1>Welcome to My Django App</h1>
    </body>
    </html>
    """
    return HttpResponse(html_content)


class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

