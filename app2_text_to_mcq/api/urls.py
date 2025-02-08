from django.urls import path 
from .import views

urlpatterns = [
    path('', views.generate_mcq, name='text_to_mcq'),
]
