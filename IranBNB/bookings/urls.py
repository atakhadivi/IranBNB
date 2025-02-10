from django.urls import path
from .views import destination_search

urlpatterns = [
    path('search-destination/', destination_search, name='destination_search'),
]
