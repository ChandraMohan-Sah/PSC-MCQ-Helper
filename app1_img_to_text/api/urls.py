from django.urls import path 
from .import views

urlpatterns = [
    path("", views.ocr_view, name="ocr_view"),
    path('download_txt/', views.download_txt, name='download_txt'),

]
