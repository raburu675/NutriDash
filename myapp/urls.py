# myapp/urls.py

from django.urls import path
from . import views
# app_name = 'myapp' #
urlpatterns = [
    # Map the root URL of your app to the 'home' view
    path('', views.home, name='home'), 
    
    #Map the settings URL to the 'settings' view
    path('settings/', views.settings, name='settings'), 
]