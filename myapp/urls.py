# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'), # Maps the root URL of the app to the 'index' view
]