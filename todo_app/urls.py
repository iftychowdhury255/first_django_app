from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-data/', views.add_data, name='add_data')
]
