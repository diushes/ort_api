from django.urls import path
from .views import TestListView, TestsByCategoryListView

urlpatterns = [
    path("tests/", TestListView.as_view(), name="tests"),
    path('testsbycategory/<int:category_id>/', TestsByCategoryListView.as_view(), name='tests-by-category-list'),
]
