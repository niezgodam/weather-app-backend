from django.urls import path
from .views import WeatherParameters


urlpatterns = [
    path('<str:latitude>/<str:longitude>/', WeatherParameters.as_view(), name='weather-list'),
]
