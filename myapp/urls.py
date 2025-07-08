# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Maps the root URL of the app to the 'index' view
]