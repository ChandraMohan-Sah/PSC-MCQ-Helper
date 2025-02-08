"""
URL configuration for GK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app3_exam.api import google_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complete/google/', google_auth.google_callback, name='google_callback'),

    path('', include("home.api.urls")),
    path('app1_img_to_text/', include("app1_img_to_text.api.urls")),
    path('app2_text_to_mcq/', include("app2_text_to_mcq.api.urls")),
    path('app3_exam/', include("app3_exam.api.urls")),
    path('app4_leaderboard/', include("app4_leaderboard.api.urls")),
    path('app6_upload_question/', include("app6_upload_question.api.urls")),
]
