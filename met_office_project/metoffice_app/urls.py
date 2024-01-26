# urls.py
from django.urls import path
from .views import get_metoffice_data

urlpatterns = [
    path('metoffice_data/', get_metoffice_data, name='get_metoffice_data'),
]
