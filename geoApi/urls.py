from django.urls import path
from .views import  GeoLocation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(GeoLocation.as_view()))
]
