
from django.urls import path
from .views import wine_list, wine_details

urlpatterns = [
    path('wines/', wine_list),
    path('wines/<int:pk>/', wine_details),
]