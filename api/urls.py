
from django.urls import path

# Class Based API
from .views import WineList, WineDetails

# Fucntion Based API
# from .views import wine_list, wine_details

urlpatterns = [

    # Class Based API
    path('wines/', WineList.as_view()),
    path('wines/<int:id>/', WineDetails.as_view())

    # Function Based API
    # path('wines/', wine_list),
    # path('wines/<int:pk>/', wine_details),

]