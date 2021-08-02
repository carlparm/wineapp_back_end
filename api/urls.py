
from django.urls import path
from .views import wine_list

urlpatterns = [
    path('wines', wine_list),
]