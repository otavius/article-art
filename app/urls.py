from django.urls import path 
from app.views import home

urlpatterns = [
    path("", home),
]