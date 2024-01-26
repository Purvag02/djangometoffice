# metoffice_app/urls.py

from django.urls import path
from .views import get_metoffice_data, metoffice_data_ui

urlpatterns = [
    path('metoffice_data/', get_metoffice_data, name='get_metoffice_data'),
    path('metoffice_data_ui/', metoffice_data_ui, name='metoffice_data_ui'),
]
