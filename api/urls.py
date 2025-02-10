from django.urls import path
from . import views

urlpatterns = [
    path('generate_password' , views.generate_password),
    path('random_number' , views.random_number),
    path('weather_info' , views.weather_info)
]
