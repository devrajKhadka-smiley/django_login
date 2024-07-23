from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up/', views.sign_up, name="sign-up"),
    path('sign-in/', views.sign_in, name="sign-in"),
    path('sign-out/', views.sign_out, name="sign-out"),
]
