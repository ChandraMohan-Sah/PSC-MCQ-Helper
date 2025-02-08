from django.urls import path 
from .import views


#Google Auth
from .import google_auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.exam, name="exam"),
    path('login/google/', google_auth.google_login, name='google_login'),
    path('logout/', views.custom_logout_view, name='logout' ),
    path('exam/status/', views.exam_status, name='exam_status'),
    path('exam/take/<str:exam_date_str>/', views.take_exam, name='take_exam'),
    path('review_exam/<str:exam_date_str>/', views.review_exam, name='review_exam'),

]
